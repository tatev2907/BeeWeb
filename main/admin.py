from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import URLs

admin.site.register(URLs)
admin.site.register(User)
