from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Tech With Sunday!!!!!</h1>")

def home(response):
    return HttpResponse("<h1>Tech With Baby Ruby!!!!!</h1>")