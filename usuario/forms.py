from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class kingForm(UserCreationForm):
    full_name = forms.CharField(label='Nome Completo:', max_length=100)
    rg = forms.CharField(label='Rg:', max_length=20)
    cpf_cnpj = forms.CharField(label='Cpf ou Cnpj:', max_length=20) 
    phone = forms.CharField(label='Telefone:', max_length=20)
    email = forms.CharField(label='Email:', max_length=100)
    job = forms.CharField(label='Ocupação:', max_length=100)
    andreess = forms.CharField(label='Endereço:', max_length=100)

    class Meta:
        model = User
        fields = ('username','rg','cpf_cnpj','phone','email','job','andreess','password1','password2')

class LoginForm(forms.Form):
    user = forms.CharField(label='User:', max_length=100)
    password = forms.CharField(label='Password:', max_length=100)