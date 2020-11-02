from django.forms import ModelForm
from .models import *
from django import forms


class FbForm(ModelForm):
    class Meta:
        model = Fbuser

        fields = ['fb_name', 'fb_email', 'fb_password','fb_dp']
        widgets = {
            'fb_name': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fb_password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'fb_age': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_dp': forms.FileInput(attrs={'class': 'form-control'}),
        }

        def clean(self):
            pass