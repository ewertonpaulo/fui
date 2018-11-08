from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import User_animal
from django.contrib.auth.decorators import login_required
from perfil.forms import edit_photo_form
# Create your views here.

@login_required
def perfil(request):
    form = edit_photo_form()
    user = request.user
    user_animal = User_animal.objects.get(user=user.id)
    if user_animal.type == 'Animal':
        return render(request, 'home/index.html', { 'user_animal':user_animal, 'form': form})
    else:
        return render(request, 'perfil/perfil_king.html', { 'user_animal':user_animal, 'form': form})


def add_photo(request):
    if request.method == 'POST':
        form = edit_photo_form(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user_animal = User_animal.objects.get(user=user.id)
            user_animal.photo = form.cleaned_data['photo']
            user_animal.save()
            return redirect('perfil')
    else:
        form = edit_photo_form()
    return render(request, 'perfil/perfil_king.html', {'form':form})
