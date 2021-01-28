from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDolist,Item

# Create your views here.
def index(response, id):
    ls = ToDolist.objects.get(id =id)
    return render(response, 'main/base.html', {})

def home(response):
    return render(response, 'home/base.html', {})