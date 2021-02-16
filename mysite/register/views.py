from django.shortcuts import render,redirect
from.forms import RegisterForm
# Create your views here.
def index(response):  
    if response.method == "POST": 
        form = RegisterForm(response.POST)
        if form.is_valid(): 
            form.save()
        return redirect("/home")
    else: 
        form = RegisterForm()
    return render(response, 'register/index.html', {'form':form})