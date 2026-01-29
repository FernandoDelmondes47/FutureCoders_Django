from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('escolha_galaxia/', views.escolhaGalaxia_view, name='escolha_galaxia'),
    path('galaxia_back/', views.galaxia_back_view, name='galaxia_back'),
    path('galaxia_front/', views.galaxia_front_view, name='galaxia_front'),


    #planetas front
    path('planeta_html/', views.construcao_view, name='planeta_html'),
    path('planeta_css/', views.construcao_view, name='planeta_css'),
    path('planeta_javascript_web/', views.construcao_view, name='planeta_javascript_web'),
    path('planeta_vue/', views.construcao_view, name='planeta_vue'),

    #planetas back
    path('planeta_construcao/', views.construcao_view, name='planeta_construcao'),
    path('planeta_javascript/', views.planeta_javascript_view, name='planeta_javascript_back'),

    
    
    #conteudos
    path('conteudo/', views.conteudo_view, name='conteudo'),

    #exercicios
    path('exercicios_javascript_back/', views.exercicios_javascript_back_view, name='exercicios_javascript_back'),
    path('exercicios_javascript_back_code/', views.exercicios_javascript_back_code_view, name='ex_conceitos_iniciais_code'),
    path('acertar_resposta/', views.acerto_resposta_view, name='acertar_resposta'),
    path('errar_resposta/', views.erro_resposta_view, name='errar_resposta'),
    path('acertar_resposta_1/', views.acerto_resposta1_view, name='acertar_resposta_1'),
    path('errar_resposta_1/', views.erro_resposta1_view, name='errar_resposta_1'),
]
