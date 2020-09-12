from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Order_form(ModelForm):
    class Meta:
        model=orderStatus
        fields='__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
