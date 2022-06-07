
from django.contrib import admin
from .models import certificates, usrinfo,fields,Question
@admin.register(usrinfo)
class usrinfoadmin(admin.ModelAdmin):
    list_display=['usr','fdsneeded_list','fdsexpert_list']
@admin.register(fields)
class fieldsadmin(admin.ModelAdmin):
    list_display=['name','guides_list','guidees_list']
# Register your models here.

admin.site.register(certificates)
admin.site.register(Question)
