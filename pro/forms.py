from django import forms
from django.core import validators
from django.contrib.auth.models import User
from pro.models import UserProfile
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email','password']





