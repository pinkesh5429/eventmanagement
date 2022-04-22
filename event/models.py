from asyncio.windows_events import NULL
from distutils.command.upload import upload
import email
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
    
class User(AbstractUser):
    gender = (
        ('male','Male'),
        ('female', 'Female'),
    )
    role = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    roles = models.CharField(max_length=10, choices=role)
    genders = models.CharField(max_length=6, choices=gender)
    image = models.ImageField(null=True, blank=True, upload_to="documents/")
    request=models.BooleanField(default=False)
    # is_student = models.BooleanField('Is Student', default=False)
    # is_teacher = models.BooleanField('Is Teacher', default=False)


class profile(models.Model):
    gender = (
        ('male','Male'),
        ('female', 'Female'),
    )
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    username = models.CharField('Username', max_length=100,null=True, blank=True)
    email = models.EmailField('Email Id', max_length=100)
    genders = models.CharField(max_length=6, choices=gender)
    image = models.ImageField(null=True, blank=True, upload_to="documents/")

# class ProfileImage(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     image = models.ImageField(null=True, blank=True, upload_to="documents/")
#     def __str__(self):
#         return self.image

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField('Venue',max_length=120)
    description = models.TextField(blank=True)
    event_image = models.ImageField(null=True, blank=True, upload_to="documents/event")
    username=models.CharField('username',null=True,max_length=120)
    def __str__(self):
        return self.name
    
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped
    
    def Is_Past(self):
        today = date.today()
        if self.event_date.date() < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)