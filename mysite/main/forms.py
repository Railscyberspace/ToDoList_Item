from django import forms
    
class CreateNewList(forms.Form):  
    lastname = forms.CharField(label="LastName", max_length=200)
    surname = forms.CharField(label="SurName", max_length=200)
    check = forms.BooleanField(required=False)   
 
    
    