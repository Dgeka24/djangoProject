from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateCVForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    skills = forms.CharField(label="Skills", max_length=500)
    interests = forms.CharField(label="Interests", max_length=500)
    education = forms.CharField(label="Education", max_length=500)
    experience = forms.CharField(label="Experience", max_length=500)