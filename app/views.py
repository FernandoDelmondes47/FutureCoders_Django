from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def cadastro_view(request):
    return render(request, 'cadastro.html')

def escolhaGalaxia_view(request):
    return render(request, 'escolha_galaxia.html')