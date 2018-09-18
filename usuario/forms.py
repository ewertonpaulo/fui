from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import King

class kingForm(ModelForm):
    username = forms.CharField(label='Nome de usuario:', max_length=100)
    password = forms.CharField(label='senha:', max_length=30)
    email = forms.CharField(label='Email:', max_length=100)
    full_name = forms.CharField(label='Nome Completo:', max_length=100)
    rg = forms.CharField(label='Rg:', max_length=20)
    cpf_cnpj = forms.CharField(label='Cpf ou Cnpj:', max_length=20)
    phone = forms.CharField(label='Telefone:', max_length=20)
    adress = forms.CharField(label='Endereço:', max_length=100)



    class Meta:
        model = King
        fields = ('username','full_name','rg','cpf_cnpj','phone','email','adress','password')

class LoginForm(forms.Form):
    user_name = forms.CharField(label='User:', max_length=100)
    password = forms.CharField(label='Password:', max_length=100)