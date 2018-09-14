from django.shortcuts import render, redirect
from rest_framework import viewsets, serializers
from .models import King
from .serializers import KingSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import LoginForm, kingForm

# Create your views here.

class KingViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = King.objects.all()
        serializer = KingSerialize(queryset, many = True)
        return Response(serializer.data)

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse('Logado')
    else:
        form = LoginForm()
    context_dict = {'form': form}
    return render(request, 'index.html', context=context_dict)

def signUp(request):
    if request.method == 'POST':
        form = kingForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = kingForm()
    return render(request, 'registration/singup.html', {'form': form})

