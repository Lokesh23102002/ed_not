from unicodedata import name
from django.urls import path
from .views import gde_cntct_lst, gdeprofile
urlpatterns = [

    path('<str:field>/guidees_contacted',gde_cntct_lst,name='gde_contacted'),
    path('<field>/guidee/<guidee>', gdeprofile, name='guidee_profile')
]