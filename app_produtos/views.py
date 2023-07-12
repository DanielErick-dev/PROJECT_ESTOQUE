from django.shortcuts import render, redirect, get_object_or_404
from .models import Alimentos
from .forms import AlimentoForm, PedidoForm
from django.http import Http404, HttpResponse
pedidos = []
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
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            print('novo objeto salvo no banco de dados')
            return redirect('app_produtos:exibir_estoque')
    else:
        form = AlimentoForm()
    return render(request, 'vizualizar_estoque.html', {'form': form})

def exibir_produtos_venda(request):
    produtos = Alimentos.objects.all()
    form = PedidoForm()
    contexto = {'produtos': produtos, 'form':form}
    return render(request, 'itens_para_venda.html', contexto)

def processar_resposta(request):
    if request.method == 'POST':
        resposta = request.POST.get('resposta', '')
        try:
            produto = get_object_or_404(Alimentos, nome=resposta)
            return render(request, 'tela_de_compra.html', {'produto': produto})
        except Http404:
            return resultado_nao_esperado(request)
    else:
        return resultado_nao_esperado(request)
def resultado_nao_esperado(request):
    mensagem = 'o item não está disponivel no estoque ou a digitação do produto está errada'
    return render(request, 'resultado_nao_esperado.html', {'mensagem': mensagem})

def adicionar_pedido(request):
    if request.method == 'POST':
        produto = request.POST.get('nome', '')
        quantidade = request.POST.get('quantidade', '')

        if produto and quantidade:
            pedido = {'produto': produto,
                      'quantidade': quantidade}
            pedidos = request.session.get('pedidos', [])
            pedidos.append(pedido)

            request.session['pedidos'] = pedidos
    return redirect('app_produtos:exibir_produtos_venda')

def finalizar_pedido(request):
    pedidos = request.session.get('pedidos', [])
    total = 0
    for pedido in pedidos:
        produto = Alimentos.objects.get(nome=pedido['produto'])
        quantidade = int(pedido['quantidade'])
        total += produto.preco * quantidade

    contexto = {'pedidos': pedidos, 'total':total}
    del request.session['pedidos']
    return render(request, 'finalizar_pedido.html', contexto)





