from django import forms

from .import models


class donate_form(forms.ModelForm):
    class Meta:
        model = models.Donate
        fields = "__all__"