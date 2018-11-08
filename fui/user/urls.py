from django.contrib import admin
from user import views
from django.urls import path
from django.conf.urls import include
from profile import urls as profile_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('profile/', include(profile_urls)),
    path('', views.signup_user, name = 'signup'),
    path('delete_user', views.delete_user, name = 'delete_user')

]+ static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)