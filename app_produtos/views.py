from django.shortcuts import render
from .models import Alimentos

def exibir_estoque(request):
    alimentos = Alimentos.objects.all()
    dicionario_alimentos = {
        'alimentos': alimentos
    }
    return render(request, 'vizualizar_estoque.html', dicionario_alimentos)

def exibir_pagina_inicial(request):
    alimentos = Alimentos.objects.all()
    dicionario_alimentos = {'alimentos': alimentos}

    return render(request, 'pagina_inicial.html', dicionario_alimentos)
