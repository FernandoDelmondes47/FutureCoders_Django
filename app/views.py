from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def cadastro_view(request):
    return render(request, 'cadastro.html')

def escolhaGalaxia_view(request):
    return render(request, 'escolha_galaxia.html')

def galaxia_back_view(request):
    return render(request, 'galaxia_back.html')

def galaxia_front_view(request):
    return render(request, 'galaxia_front.html')

def construcao_view(request):
    return render(request, 'planeta_construcao.html')

def planeta_javascript_view(request):
    return render(request, 'planeta_javascript_back.html')

def conteudo_view(request):
    return render(request, 'conteudos/javascript_back/conceitos_da_linguagem.html')