# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from datetime import *
import json
import os

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    email_address = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                     label=("Email address"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
                               label=("Password"))
    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=("Password Again"))

    def save(self):
        if self.is_valid():
            data = self.cleaned_data
            if self.cleaned_data['password'] == self.cleaned_data['password_again']:
                new_user=User.objects.create_user(self.cleaned_data['username'],
                                  self.cleaned_data['email_address'],
                                  self.cleaned_data['password'])
                new_user.save()

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {
            'class': "form-control",
            'placeholder': "username"
        }
        ),

        self.fields['email_address'].widget.attrs.update(
        {
            'class': "form-control",
            'placeholder': "e-mail address"
        }
        ),

        self.fields['password'].widget.attrs.update(
        {
            'class': "form-control",
            'placeholder': "password"
        }
        ),

        self.fields['password_again'].widget.attrs.update(
        {
            'class': "form-control",
            'placeholder': "password again"
        }
        ),