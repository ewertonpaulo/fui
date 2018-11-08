from django.urls import path

from perfil.views import perfil, add_photo

urlpatterns = [
    path('', perfil, name='perfil'),
    path('edit_photos', add_photo, name='edit_photo')
]