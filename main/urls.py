from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search')
]
