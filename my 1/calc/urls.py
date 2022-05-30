from os import name
from unittest.mock import patch
from django.urls import path
from django.contrib.auth import views as vp
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    
    path('signup/',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('dash',views.dash,name="dash"),
    path('Guide',views.guide,name="guide"),
    path('verify/<token>' , views.verify , name="verify"),
    path('password_reset/', vp.PasswordResetView.as_view(template_name='password_reset/forgot_mail.html'), name='password_reset'),
    path('password_reset_done/', vp.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',vp.PasswordResetConfirmView.as_view(template_name='password_reset/forgot_change_pass.html'),name='password_reset_confirm'),
    path('password_reset_complete/',vp.PasswordResetCompleteView.as_view(template_name='password_reset/forgot kuch kuck.html'), name='password_reset_complete')


]