from django import forms

class NameForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
   
    age = forms.IntegerField(label='age')
    
    email = forms.EmailField(label='email')