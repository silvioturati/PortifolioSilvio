from django.shortcuts import render, get_object_or_404
from .models import Projeto


def index(request):
    return render(request, 'portifolioprojetos/index.html')


def portifolioprojetos(request):

    # o código abaixo foi usado para listar os projetos na página de projetos antes de usarmos o BD
    # projetos ={
    #     1: 'Usando Selenium',
    #     2: 'Usando Dicionários em Python 3',
    #     3: 'Usando Listas em Python 3'
    # }
    #
    # dados = {
    #    'descricao_projetos': projetos
    # }
    # return render(request, 'portifolioprojetos/portfolio.html', dados)

    # a linha abaixo é o codígo para a mesma função usando o BD
    projetos = Projeto.objects.all()

    dados = {
        'projetos': projetos,
    }

    return render(request, 'portifolioprojetos/portfolio.html', dados)


def portifoliodetails(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)

    dados = {
        'projeto': projeto
    }

    return render(request, 'portifolioprojetos/portfolio-details.html', dados)
