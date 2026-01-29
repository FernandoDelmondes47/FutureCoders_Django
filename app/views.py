from django.shortcuts import redirect, render

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
    return render(request, 'planetas/planeta_construcao.html')

#planetas
def planeta_javascript_view(request):
    return render(request, 'planetas/planeta_javascript_back.html')

def conteudo_view(request):
    return render(request, 'conteudos/javascript_back/conceitos_da_linguagem.html')





#exercicios

def acerto_resposta_view(request):
    return render(request, 'exercicios/acerto_resposta.html')

def erro_resposta_view(request):
    return render(request, 'exercicios/erro_resposta.html')

def acerto_resposta1_view(request):
    return render(request, 'exercicios/acerto_resposta1.html')

def erro_resposta1_view(request):
    return render(request, 'exercicios/erro_resposta1.html')

def exercicios_javascript_back_view(request):
    if request.method == 'POST':
       resposta = request.POST.get('opcao_escolhida')
       if resposta == 'C':
           return redirect('acertar_resposta')
       elif resposta in ['A', 'B', 'D']:
           return redirect('errar_resposta')
    return render(request, 'exercicios/javascript_back/ex_conceitos_iniciais.html')

def exercicios_javascript_back_code_view(request):
    if request.method == 'POST':
        # Aqui você pode processar os dados enviados pelo formulário
        resposta = request.POST.get('opcao_escolhida')
        if resposta == 'B':
            return redirect('acertar_resposta_1')
        elif resposta in ['A', 'C', 'D']:
            return redirect('errar_resposta_1')
        # Lógica para verificar a resposta e fornecer feedback pode ser adicionada aqui
    return render(request, 'exercicios/javascript_back/ex_conceitos_iniciais_code.html')