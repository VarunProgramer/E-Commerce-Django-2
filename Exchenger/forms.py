from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CodegeryForm(forms.ModelForm):
    name = forms.TextInput()
    codegery_image = forms.ImageField()
    description = forms.TextInput()
    class Meta:
        model = codegery
        fields = ['name', 'codegery_image', 'description']
class ProdectForm(forms.ModelForm):
    name = forms.TextInput()
    prodect_image = forms.ImageField()
    more_prodect_image = forms.ImageField()
    description = forms.Textarea()
    codegery_type = forms.TextInput()
    class Meta:
        model = prodect
        fields = ['name', 'prodect_image','more_prodect_image','price', 'description', 'codegery_type']
        
