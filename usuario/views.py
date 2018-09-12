from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import King
from .serializers import KingSerialize

# Create your views here.

class KingAPI(viewsets.ModelViewSet):
    queryset = King.objects.all()
    serializer_class = KingSerialize
    