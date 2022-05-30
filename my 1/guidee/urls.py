from django.urls import path, include

from .views import fdgdlst, gdprofile

urlpatterns=[
    path('<str:field>/guidelist',fdgdlst, name='gdlst'),
    path('<str:field>/<str:guide>', gdprofile, name='gdprofile'),
]