from unicodedata import name
from django.urls import URLPattern, path
from . import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.splashscreen, name="splashscreen"),
    path('ulogin', views.login, name="login"),
    path('usignup', views.signup, name="signup"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout_user,name="logout_user"),
    path('uregistered', views.registereduser, name="registereduser"),
    path('registerotp', views.rotp, name="otp"),
    path('emailver', views.emailverification, name="emailver"),
    path('authordash', views.authordash, name="authordash"),
    path('authorprofile/<user_id>', views.authorprofile, name="authorprofile"),
    path('userdash', views.userdash, name="userdash"),
    path('add_event', views.add_event, name="add-event"),
    path('edit_event/<event_id>', views.edit_event, name="edit_event"),
    path('teacher_edit_event/<event_id>',views.teacher_edit_event,name="teacher_edit_event"),
    path('delete_event/<event_id>', views.delete_event, name="delete_event"),
    path('aevent_list',views.aevent_list,name="aevent_list"),
    path('manageuser',views.manageuser,name='manageuser'),
    path('delete_user/<user_id>', views.delete_user, name="delete_user"),
    path('userrequest',views.userrequest,name="userrequest"),
    path('approve_user/<user_id>',views.approve_user,name="approve_user"),
    path('userallevents',views.userallevents,name="userallevents"),
    path('register_event',views.register_event,name="register_event"),
    path('seefull_event/<event_id>',views.seefull_event,name="seefull_event"),
    path('event_list', views.event_list, name="event_list"),
    path('teacherdash', views.teacherdash, name="teacherdash"),
    path('teacherprofile/<user_id>', views.teacherprofile, name="teacherprofile"),
    path('userprofile/<user_id>', views.userprofile, name="userprofile"),
    path('paynow',views.paynow,name="paynow"),
    path('cart',views.cart,name="cart"),
    path('handlerrequest',views.handlerrequest,name="handlerrequest"),
    path('pdf',views.pdf,name="pdf"),
    path('registeredotp',views.send_otp,name="registerotp"),
    path('otpverify',views.retriveotp,name="retriveotp"),
    path('passchange',views.passchange,name="passchange"),
    path('passwordchange',views.passwordchange,name="passwordchange"),
    path('verifyforgototp',views.verifyforgototp,name="verifyforgototp"),
    path('addtocart/<event_id>',views.addtocart,name="addtocart"),
    path('seeattendee',views.seeattendee,name="seeattendee"),
    path('seeattendee/attendeelist',views.attendeelist,name="attendeelist"),
    path('teacheraddevent',views.teacheraddevent,name="teacheraddevent"),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)