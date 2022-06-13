from sys import implementation
import django
from django.contrib import admin

from .models import  room, message

admin.site.register(room)
admin.site.register(message)