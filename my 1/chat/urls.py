from django.urls import path, include

from .views import rm

app_name='chat'

urlpatterns=[
    path('<str:other_usr>/', rm, name='room'),
]