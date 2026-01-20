from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('escolha_galaxia/', views.escolhaGalaxia_view, name='escolha_galaxia'),
]
