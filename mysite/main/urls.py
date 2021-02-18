from django.urls import path
from  . import  views

urlpatterns = [
     path("home/", views.home, name = "home"),
    path("<int:id>", views.index, name = "index"),
    path("create/", views.create, name = "create"),
    path("List/", views.create, name = "List"),
  
  
]

