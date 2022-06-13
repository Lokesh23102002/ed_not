
from django.contrib import admin
from .models import usrinfo,fields,Question,Review,Rating
@admin.register(usrinfo)
class usrinfoadmin(admin.ModelAdmin):
    list_display=['usr']
@admin.register(fields)
class fieldsadmin(admin.ModelAdmin):
    list_display=['name']
# Register your models here.

admin.site.register(Question)
admin.site.register(Review)
admin.site.register(Rating)
