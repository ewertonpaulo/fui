from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label='User:', max_length=100)
    password = forms.CharField(label='Password:', max_length=100)