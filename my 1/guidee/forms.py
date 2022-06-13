from cProfile import label
from dataclasses import fields
from pyexpat import model
from turtle import fd
from django import forms
from django.forms import ModelForm 

from .models import fields as fds
from guide.models import Certificate

from calc.models import Review
class Rvw_form(forms.Form):
    Rvw=forms.CharField(label='Your review', widget=forms.Textarea())
   