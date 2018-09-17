from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import singUp, login, home


urlpatterns = [
    path('home/', home, name='home'),
    path('cadastro-king/', singUp, name='cadastro-king')

] + static(settings.MEDIA_URL, dcument_root = settings.MEDIA_ROOT)