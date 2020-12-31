from django.contrib import admin
from .models import Projeto

# Register your models here.
class ListandoProjetos(admin.ModelAdmin):
    """
    Classe para mudar o layout da lista de  projetos no admim
    """
    list_display = ('id', 'nome_projeto', 'linguagem') # alterando as colunas do display
    list_display_links = ('id', 'nome_projeto') # transformando o nome do projeto em link clicavel
    search_fields = ('nome_projeto', 'detalhes_projeto') # inserindo uma barra de pesquisa (a virgula é porque é uma tupla)
    list_filter = ('cliente', )
    list_per_page = 20

admin.site.register(Projeto, ListandoProjetos)