from django.urls import path, include

from .views import gdlst, gdprofile, r_queslst

urlpatterns=[

    path('<str:field>/guidelist',gdlst, name='gdlst'),
    path('<str:field>/relatedqueslst',r_queslst, name='r_queslst'),
    path('guidecontactlist',gdlst, name="gdcontactlst"),
    path('<str:field>/<str:guide>', gdprofile, name='gdprofile'),
    
]