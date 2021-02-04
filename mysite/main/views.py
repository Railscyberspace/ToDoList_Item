from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList
#from .login import LoginPage

# Create your views here.
def index(response, id = 1):
    ls = ToDoList.objects.get(id =id)
    return render(response, 'main/List.html',{'ls':ls})

def home(response):
    return render(response, 'main/home.html',{})

def create(response):  
    if response == "POST": 
        form = CreateNewList(response.POST)
        if form.is_valid():  
            n = form.cleaned_data['lastname']
            t = ToDoList(lastname = n)
            t.save()
        return HttpResponseRedirect('/%i' %t.id)
    else:  
        form = CreateNewList()
    return render (response, 'main/create.html',{'form':form})


