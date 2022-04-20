
from django.contrib import admin
from .models import certificates, calc,fields
@admin.register(calc)
class calcadmin(admin.ModelAdmin):
    list_display=['user','fdsneeded_list','fdsexpert_list']
@admin.register(fields)
class fieldsadmin(admin.ModelAdmin):
    list_display=['name','guides_list','guidees_list']
# Register your models here.

admin.site.register(certificates)
