from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm
# Create your models here.

class Personal_Info(models.Model):
    email = models.EmailField(_('Email address'),max_length=100,blank=True,)
    phone1 = models.CharField(_('Phone Number1'),max_length=15,blank=True,null=True)
    phone2 = models.CharField(_('Phone Number1'), max_length=15, blank=True, null=True)
    address = models.TextField(_('Address'), max_length=100, blank=True, null=True)
    date_time = models.DateTimeField(_('Date Time'),auto_now_add=True)

# class CommenttForm(forms.Form):
#   Search=Fo.CharField(label='search',
#                     widget=forms.TextInput(attrs={'placeholder': 'Search'}))


