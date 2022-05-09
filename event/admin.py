from django.contrib import admin
from .models import Cart, User, Event,profile,Transaction

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(profile)
admin.site.register(Transaction)
admin.site.register(Cart)