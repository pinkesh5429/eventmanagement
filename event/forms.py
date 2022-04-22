from cProfile import label
from pyexpat import model
from random import choices
from xml.dom.minidom import Attr
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import HiddenInput, ModelForm
from django.contrib.auth import login, authenticate
from .models import User, Event, profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

gender = (
        ('male','Male'),
        ('female', 'Female'),
    )

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    # roles = forms.Select(choices=role, attrs={'class':'form-control'})
    genders = forms.Select(choices=gender, attrs={'class':'form-control',})
    image = label
    {
        'image':''
    }

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'roles', 'genders', 'image']

# class UserRegistrationForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'roles', 'genders', 'image')
#         labels = {
#             'first_name': 'First Name',
#             'last_name': 'Last Name',
#             'username': 'Username',
#             'email': 'Email Id',
#             'password1': 'Password',
#             'password2': 'Confirm Password',
#             'roles': 'Role',
#             'genders': 'Gender',
#             'image': ''		
#         }
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
#             'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
#             'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Id'}),
#             'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
#             'password2': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'})
#         }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'description', 'event_image','username')
        labels = {
            'name': 'Event Name',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'Venue',
            'description': 'Description',
            'event_image': '',
            'username':''		
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
            'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
            'username': forms.HiddenInput(attrs={'class':'form-control'}),
            
        }

class ProfileForm(ModelForm):
    class Meta:
        model=profile
        fields = ['first_name', 'last_name', 'username', 'email', 'genders', 'image']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email Id',
            'genders': 'Gender',
            'image': ''		
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Id'}),
           
        }

