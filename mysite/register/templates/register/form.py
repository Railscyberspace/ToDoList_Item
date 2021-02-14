
from django.models  import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):  
    Email = models.EmailField()