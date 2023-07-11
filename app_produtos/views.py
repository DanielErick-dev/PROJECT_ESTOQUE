from django.shortcuts import render, redirect
from .models import Alimentos
from .forms import AlimentoForm

def exibir_estoque(request):

    alimentos = Alimentos.objects.all()
    form = AlimentoForm()
    dicionario_alimentos = {
        'alimentos': alimentos, 'form': form
    }

    return render(request, 'vizualizar_estoque.html', dicionario_alimentos)

def exibir_pagina_inicial(request):
    alimentos = Alimentos.objects.all()
    dicionario_alimentos = {'alimentos': alimentos}

    return render(request, 'pagina_inicial.html', dicionario_alimentos)

def adicionar_alimento(request):
    print('entrou na views exibir_estoque')
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            print('novo objeto salvo no banco de dados')
            return redirect('app_produtos:exibir_estoque')
    else:
        form = AlimentoForm()
    return render(request, 'vizualizar_estoque.html', {'form': form})