from django import forms
from .import models

# class Personal_InfoForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(Personal_InfoForm, self).__init__(*args,**kwargs)
#     class Meta:
#         model = models.Personal_Info
#         fields = ('email', 'phone1', 'phone2', 'address')
#         email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input','placeholder':'email'})),
#
#         # phone1 = forms.TextInput(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'email'})),
#         # phone2 = forms.TextInput(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'email'})),
#         # address = forms.TextInput(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'email'}))
#
#         # widgets = {
#         #     'email':forms.EmailField(attrs={'class':'input','placeholder':'email'}),
#         #     'phone1':forms.TextInput(attrs={'class':'input','placeholder':'phone1'}),
#         #     'phone2':forms.TextInput(attrs={'class':'input','placeholder':'phone2'}),
#         #     'address':forms.TextInput(attrs={'class':'input','placeholder':'address'}),
#         # }
#         #
#         #

class Personal_InfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Personal_InfoForm, self).__init__(*args, **kwargs)
    class Meta:
        model = models.Personal_Info
        fields = '__all__'
        widgets = {
            'phone1' : forms.TextInput(attrs = {'placeholder': 'Username'}),
            'email'  : forms.TextInput(attrs = {'placeholder': 'E-Mail'}),
        }