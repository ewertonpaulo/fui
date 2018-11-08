from django import forms
from user.models import User_animal

class edit_photo_form(forms.Form):
    photo = forms.ImageField()

    class meta:
        model = User_animal
        fields = ['photo']
