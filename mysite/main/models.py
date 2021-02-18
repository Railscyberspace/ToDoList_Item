from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "ToDoList", null = True),
    name = models.CharField(max_length =200)
    
    def _str_(self):
        return self.name
    
    
class Item(models.Model):
        todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
        text =models.CharField(max_length =300)
        complete = models.BooleanField()
        
        def _str_(self):
            return self.name.text
        