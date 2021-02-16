
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):  
    Email = forms.EmailField()
    
class Meta: 
    model = User
    field = ["Username", "password1", "password2"]
    
    
    
    