from ast import Continue
from email.mime import image
import imp
from os import name
from random import random
import re
from sre_constants import SUCCESS
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views import generic
from pkg_resources import register_loader_type
from .models import Event, Transaction, User,Cart
from .forms import ProfileForm, TransactionForm, UserRegistrationForm, EventForm,CartForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import math
import random
import json
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render
from django.core.mail import send_mail


from PayTm import Checksum
MERCHANT_KEY = '5TlAF_WmbU94ay#c'
# Create your views here.

#splashscreen
def splashscreen(request):
    return render(request, 'splashscreen.html')

#For Login 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(request, username=username, password=password1)
        # type_obj = user_type.objects.get(user=user)
        if user is not None and user.roles == 'student' and user.otpverify==True:
            auth_login(request, user)
            return redirect('userdash')
        elif user is not None and user.roles == 'teacher' and user.otpverify==True:
            auth_login(request, user)
            return redirect('teacherdash')
        elif user is not None and user.roles == 'admin' and user.otpverify==True:
            auth_login(request, user)
            return redirect('authordash')
        else:
            return render(request,'ulogin.html',{'msg':"your username or password is incorrect"})
    else:
        return render(request, 'ulogin.html')

#For SignUp   
def signup(request):
    if request.method == "POST":
        global useremail     
        useremail=request.POST['email']
        global registerotp
        registerotp=generateOTP()
        htmlgen = '<p>Your OTP is <strong>'+registerotp+'</strong></p>'
        send_mail('OTP request',registerotp,'<your gmail id>',[useremail], fail_silently=False, html_message=htmlgen)
        # return render(request,'otppage.html')
    
                

        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # print("uptovalid")
            form.save()
            # print("uptosave")
            return render(request,'otppage.html')
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # auth_login(request, user)
            # return redirect('login')
    else:
        # print("inelse")
        form = UserRegistrationForm()
    return render(request, 'uregister.html',{'form':form,})

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
    email=request.POST['registeremail']
    print(email)
    global o
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
    return render(request,'otppage.html')

    
def retriveotp(request):
    otp=request.POST['enterotp']
    # print(type(otp))
    # print(type(o))
    if registerotp==otp:
        User.objects.filter(email=useremail).update(otpverify=True)  
        return render(request,'ulogin.html')      
    else:
        return HttpResponse("otp not matched") 

def passchange(request):
    global remail
    remail=request.POST['registeremail']
    cuser=User.objects.filter(email=remail).first()
    if cuser:
        global forgotrotp
        forgotrotp=generateOTP()
        htmlgen = '<p>Your OTP is <strong>'+forgotrotp+'</strong> For Forgot Password</p>'
        send_mail('OTP request',forgotrotp,'<your gmail id>',[remail], fail_silently=False, html_message=htmlgen)
        return render(request,'forgototp.html')
        # return HttpResponse("yes user is there")
    else:
        return HttpResponse("no user is not there")

def verifyforgototp(request):
    forgototp=request.POST['forgototp']
    if forgototp==forgotrotp:
        return render(request,'passwordchange.html')
    else:
        return render(request,'forgototp.html',{'msg':'OTP Does Not Matched'})
    
    
def passwordchange(request):
    newpassword=request.POST.get('newpassword')
    renewpassword=request.POST.get('renewpassword')
    if newpassword==renewpassword:
        puser=User.objects.get(email=remail)
        puser.set_password(newpassword)
        puser.save()
        return render(request,'ulogin.html')
    else:
        return HttpResponse("not mathcedddd")
    
    

#For authorprofile
def authorprofile(request, user_id):
    profile = User.objects.get(id=user_id)
    form = ProfileForm(request.POST or None ,request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('authordash')

    return render(request, 'author/authorprofile.html', 
        {'user': profile,
        'form':form})

#For teacherprofile
def teacherprofile(request, user_id):
    profile = User.objects.get(id=user_id)
    form = ProfileForm(request.POST or None ,request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('teacherdash')

    return render(request, 'teacher/teacherprofile.html', 
        {'user': profile,
        'form':form})

#For add event
def add_event(request):
    submitted = False
    if request.method == "POST":              
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/event_list')
    else:
        form = EventForm()
        # if 'submitted' in request.GET:
        # 	submitted = True
    
    return render(request, 'author/add_event.html', {'form':form, 'submitted':submitted})

#For edit event
def edit_event(request, event_id):
    
    event = Event.objects.get(id=event_id)
    form = EventForm(request.POST or None ,request.FILES or None, instance=event)
    
    if form.is_valid():
        form.save()
        return redirect('aevent_list')

    return render(request, 'author/edit_event.html', 
        {'event': event,
        'form':form})

def teacher_edit_event(request,event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(request.POST or None ,request.FILES or None, instance=event)
    
    if form.is_valid():
        form.save()
        return redirect('event_list')

    return render(request, 'teacher/teachereditevent.html', 
        {'event': event,
        'form':form})
    
#For delete event
def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('event_list')

#For Listing all Event
def event_list(request):
    currentuser=request.user
    # print(currentuser)
    event_list = Event.objects.filter(username=currentuser).order_by('-event_date')
    # print(event_list)
    return render(request,'teacher/teacherevent_list.html',{'event_list':event_list})

def aevent_list(request):
    aevent_list=Event.objects.all().order_by('-event_date')
    return render(request,'author/event_list.html',{'event_list':aevent_list})

def manageuser(request):
    student=User.objects.filter(roles='student')
    teacher=User.objects.filter(roles='teacher')
    # print(student)
    # print(teacher)
    return render(request,'author/manageusers.html',{'students':student,'teachers':teacher})

def addtocart(request,event_id):
    eventname1=request.POST['eventname']
    eventimg=request.POST['eventimg']
    eventprice=request.POST['eventprice']
    username=request.POST['username']
    # getevent=Event.objects.get(name=eventname1)
    # print(getevent.name)
    # print(getevent.description)
    if request.method == "POST":
        form=Cart(eventid=event_id,eventname=eventname1,eventimg=eventimg,eventprice=eventprice,username=username)
        form.save()
    return HttpResponse(eventname1)

def delete_user(request,user_id):
    getuser=User.objects.get(id=user_id)
    getuser.delete()
    return redirect('manageuser')

def userrequest(request):
    getteacher=User.objects.filter(roles='teacher',request=False)
    # print(getteacher)
    return render(request,'author/userrequest.html',{'userrequest':getteacher})

def approve_user(request,user_id):
    User.objects.filter(id=user_id).update(request=True)
    # print(gett)
    # gett.request=True
    # gett.save(["request"])
    return redirect('userrequest')

def userprofile(request, user_id):
    profile = User.objects.get(id=user_id)
    form = ProfileForm(request.POST or None ,request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('userdash')

    return render(request, 'user/userprofile.html', 
        {'user': profile,
        'form':form})

def userallevents(request):
    event_list=Event.objects.all().order_by('-event_date')
    return render(request,'user/seeevents.html',{'events':event_list})

def register_event(request):
    # form = TransactionForm(request.POST)
    # if form.is_valid():
    #     form.save()
    # regevent=Event.objects.get(id=event_id)
    total=request.POST['totalamount']
    currentuser=request.user
    cuser=User.objects.get(username=currentuser)
    # print(regevent.amount)
    return render(request,'user/registerevent.html',{'total':total,'cuser':cuser})

def seefull_event(request,event_id):
    fullevent=Event.objects.filter(id=event_id)
    return render(request,'user/seefullevent.html',{'fullevent':fullevent})

def pdf(request):
    fdata=request.POST
    # print(fdata)
    oid=fdata['oid']
    tid=fdata['tid']
    tdate=fdata['tdate']
    tamount=fdata['tamount']
    # print(fdata['ORDERID'])
    template_path = 'user/pdf.html'
    context = {'oid': oid,'tid':tid,'tdate':tdate,'tamount':tamount}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="pdf_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    

def cart(request):
    global currentuser
    currentuser=request.user
    product=Cart.objects.filter(username=currentuser,paymentstatus=False)
    total_amount=0
    for i in product:
        total_amount=total_amount+i.eventprice
    return render(request,'user/usercart.html',{'products':product,'total':total_amount})

#For Logout
def logout_user(request):
    logout(request)
    return redirect('login')




def registereduser(request):
    return render(request, 'registerotp.html')

def rotp(request):
    return render(request, 'registerotp.html')

def emailverification(request):
    return render(request, "forgot.html")

def authordash(request):
    return render(request, 'author/authordash.html')

def userdash(request):
   return render(request, 'user/userdash.html')

def teacherdash(request):
    return render(request, 'teacher/teacherdash.html')

@csrf_exempt
def paynow(request):
    if request.method=="POST":
        global eventid
        eventid=request.POST.get('eid','')
        global eventname
        eventname=request.POST.get('ename','')
        global attendeename
        attendeename=request.POST.get('attendeename','')
        global attendeeemail
        attendeeemail=request.POST.get('attendeeemail','')
        global attendeephone
        attendeephone=request.POST.get('attendeephone','')
        amount=request.POST.get('amount','')

    
        param_dict={

                'MID': 'EnJsCf18378198459335',
                'ORDER_ID': str(math.floor(100000+random.random()* 900000)),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': attendeeemail,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerrequest',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'user/paytm.html', {'param_dict': param_dict})
    # print(param_dict)

    return render(request, 'user/registerevent.html')

@csrf_exempt
def handlerrequest(request):
    # currentuser1=request.user
    print(currentuser)
    if request.method=='POST':

        form = request.POST
        response_dict = {}
        for i in form.keys():
            response_dict[i] = form[i]
            if i == 'CHECKSUMHASH':
                checksum = form[i]

        verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
        if verify:
            if response_dict['RESPCODE'] == '01':
                eid=eventid
                ename=eventname
                aname=attendeename
                aemail=attendeeemail
                aphone=attendeephone
                oid=response_dict['ORDERID']
                tid=response_dict['TXNID']
                tdate=response_dict['TXNDATE']
                tamount=response_dict['TXNAMOUNT']
                # print(eid,ename,aname,aemail,aphone)
                # print(oid,tid,tdate,tamount)
                # print(response_dict)
                Cart.objects.filter(username=currentuser).update(paymentstatus=True)
                    
                # data=Transaction(eid=eid,ename=ename,aname=aname,aemail=aemail,aphone=aphone,tamount=tamount,oid=oid,tid=tid,tdate=tdate)
                # form=TransactionForm(request.POST,instance=data)
                # if form.is_valid():
                    # form.save()
                    
            else:
                print('order was not successful because ' + response_dict['RESPMSG'])
        return render(request, 'user/paymentstatus.html', {'response': response_dict})
