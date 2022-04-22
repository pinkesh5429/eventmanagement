from django.contrib import admin
from .models import User, Event,profile

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(profile)