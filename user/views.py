from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import user_form, auth_user_on, address_form, auth_user
from django.contrib.auth.models import User
from user.models import User_animal, Address
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from profile.views import edit_profile
# Create your views here.
def signup_user(request):
    if (request.method == 'POST'):
        address_f = address_form(request.POST)
        auth_f = auth_user(request.POST)
        user_f = user_form(request.POST)
        if address_f.is_valid() and user_f.is_valid():
            try:
                edit_profile(request)
            except:
                messages.error('Usuário já cadastrado')
                render(request, 'signup/signup.html')
            if auth_f.is_valid():
                user = auth_f.save(commit=False)
                user.password=make_password(auth_f.cleaned_data['password'])
                user = auth_f.save()
                address = address_f.save()
                user_anl = user_f.save(commit=False)
                user_anl.address = address
                user_anl.user = user
                user_anl.save()
                return redirect('login')
    else:
        address_f = address_form()
        user_f = user_form()
        auth_f = auth_user()
        
    context_dict = {'address_f':address_f,'user_f':user_f,'auth_f':auth_f}
    return render(request, 'signup/signup.html', context_dict)

@login_required
def update_to_king(request):
    User_animal.objects.filter(user=request.user.id).update(type='King')
    return redirect('profile')

@login_required
def delete_user(request):
    user = request.user
    usuario = User_animal.objects.get(user = user.id)
    usuario.address.delete()
    user.delete()
    usuario.delete()
    return redirect('logout')
