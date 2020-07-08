from django.urls import path
from . import views as views_usuario

urlpatterns = [
    path('', views_usuario.Login, name='login'),
    path('registro', views_usuario.register, name='registro'),
]