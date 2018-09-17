from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, serializers
from .models import King
from .serializers import KingSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import LoginForm, kingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

class KingViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = King.objects.all()
        serializer = KingSerialize(queryset, many = True)
        return Response(serializer.data)
'''
def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('Logado')
    else:
        form = LoginForm()
    context_dict = {'form': form}
    return render(request, 'index.html', context=context_dict)
'''
def singUp(request):
    if request.method == 'POST':
        form = kingForm(request.POST)
        if form.is_valid():
            king = King()
            user_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(user_name, email, password)
            king.user = User.objects.get(username=user_name)
            king.full_name = form.cleaned_data.get('full_name')
            king.rg = form.cleaned_data.get('rg')
            king.cpf_cnpj = form.cleaned_data.get('cpf_cnpj')
            king.phone = form.cleaned_data.get('phone')
            king.job = form.cleaned_data.get('job')
            king.andress = form.cleaned_data.get('andress')
            king.save()

            return redirect('cadastro-king')
    else:
        form = kingForm()
    return render(request, 'cadastro-king.html', {'form': form})
'''
def login(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('login')
'''
@login_required
def home(request):
    return render(request, 'home.html')
