from django import forms
from main.models import Rating
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Address, User_animal
from django.contrib.auth.forms import UserCreationForm

class user_form(ModelForm):
    class Meta:
        model = User_animal
        exclude = ('address','user','type',)

class address_form(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class auth_user(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'last_name','username','password']
        widgets = {
            'password':forms.PasswordInput()
        }

class auth_user_on(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'last_name','username']

class rating_user(ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
        exclude = ('type',)
