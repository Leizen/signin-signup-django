from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logado', views.login_success, name='logado')
]