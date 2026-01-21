from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('escolha_galaxia/', views.escolhaGalaxia_view, name='escolha_galaxia'),
    path('galaxia_back/', views.galaxia_back_view, name='galaxia_back'),
    path('galaxia_front/', views.galaxia_front_view, name='galaxia_front'),
    path('planeta_construcao/', views.construcao_view, name='planeta_construcao'),
    path('planeta_javascript/', views.planeta_javascript_view, name='planeta_javascript_back'),

    
    
    
    path('conteudo/', views.conteudo_view, name='conteudo'),
]
