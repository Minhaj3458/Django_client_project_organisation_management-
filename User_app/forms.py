from django import forms
from django.contrib.auth.models import User
from .import models
class Users_form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class UserProfile_form(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = "__all__"