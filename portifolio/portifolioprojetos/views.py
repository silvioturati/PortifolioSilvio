from django.shortcuts import render


def index(request):
    return render(request, 'portifolioprojetos/index.html')


def portifolioprojetos(request):

    projetos ={
        1: 'Usando Selenium',
        2: 'Usando Dicionários em Python 3',
        3: 'Usando Listas em Python 3'
    }

    dados = {
        'descricao_projetos': projetos
    }

    return render(request, 'portifolioprojetos/portfolio.html', dados)


def portifoliodetails(request):
    return render(request, 'portifolioprojetos/portfolio-details.html')
