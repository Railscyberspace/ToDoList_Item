from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList
#from .login import LoginPage

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id =id)
    
    if response.method =="POST": 
        print(response.POST)
        if response.POST.get("save"): 
            for item in ls.item_set.all(): 
                if response.POST.get("c" + str(item.id)) == "Click":  
                    item.complete = True
                else: 
                    item.complete = False
                    item.save()
                    
        elif response.POST.get("newItem"): 
             txt = response.POST.get("new")
        if len(txt) > 2:  
            ls.item_set.create(text = txt, complete = False) 
        else: 
            print('Invalid Text')
             
    return render(response, 'main/List.html',{'ls':ls})

def home(response):
    return render(response, 'main/home.html',{})

def create(response):  
    if response == "POST": 
        form = CreateNewList(response.POST)
        if form.is_valid():  
            n = form.cleaned_data['lastname']
            response.user.todolist_set.create(name = n)
          
        return HttpResponseRedirect('/%i' %ToDoList.id)
    else:  
        form = CreateNewList()
    return render (response, 'main/create.html',{'form':form})


def View(response): 
    return render(response,"main/View.html", {})  
    