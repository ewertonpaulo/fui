from django.urls import path, include
from . import views
from rest_framework import urls, routers

router = routers.DefaultRouter()
router.register('kings', views.KingViewSet, base_name='king')

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', views.home),
    path('sign/', views.signUp)
]