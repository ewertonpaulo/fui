from django import forms
from user.models import User_animal, User_wishes

class edit_photo_form(forms.Form):
    photo = forms.ImageField()

    class meta:
        model = User_animal
        fields = ['photo']

class wishes_form(forms.ModelForm):
    class Meta:
        model = User_wishes
        fields = '__all__'
        exclude = ('user',)