from django.shortcuts import render, redirect, get_object_or_404
from .models import Alimentos
from .forms import AlimentoForm, PedidoForm, PagamentoForm, RemoverAlimentoForm
from django.http import Http404
pedidos = []
def landing_page(request):
    return render(request, 'landing_page.html')


def tela_de_login(request):
    return render(request, 'tela_de_login.html')
def exibir_estoque(request):

    alimentos = Alimentos.objects.filter(quantidade=0)
    alimentos.delete()

    alimentos = Alimentos.objects.all()
    ALIMENTOS = sorted(alimentos, key=lambda x: x.nome)
    form = AlimentoForm()
    dicionario_alimentos = {
        'alimentos': ALIMENTOS, 'form': form
    }

    return render(request, 'vizualizar_estoque.html', dicionario_alimentos)


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
def remover_alimento(request):
    if request.method == 'POST':
        form = RemoverAlimentoForm(request.POST)
        resposta = request.POST.get('nome', '')

        if form.is_valid():
            try:
                produto = get_object_or_404(Alimentos, nome=resposta.upper())

                produto.delete()
                return redirect('app_produtos:exibir_estoque')


            except Http404:
                return resultado_nao_esperado(request)
        else:
            form = RemoverAlimentoForm()
    alimentos = Alimentos.objects.all()
    form = AlimentoForm()
    dicionario_alimentos = {
        'alimentos': alimentos, 'form': form
    }
    return render(request, 'vizualizar_estoque.html', dicionario_alimentos)

def exibir_produtos_venda(request):
    produtos = Alimentos.objects.all()
    PRODUTOS  = sorted(produtos, key=lambda x:x.nome)
    form = PedidoForm()
    contexto = {'produtos': PRODUTOS, 'form':form}
    return render(request, 'itens_para_venda.html', contexto)

def processar_resposta(request):
    if request.method == 'POST':
        resposta = request.POST.get('nome', '')
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
        try:
            Produto = get_object_or_404(Alimentos, nome=produto)
            if produto and quantidade:
                pedido = {'produto': produto,
                          'quantidade': quantidade}
                pedidos = request.session.get('pedidos', [])
                pedidos.append(pedido)

                request.session['pedidos'] = pedidos
        except Http404:
            return resultado_nao_esperado(request)

    return redirect('app_produtos:exibir_produtos_venda')

def finalizar_pedido(request):
    pedidos = request.session.get('pedidos', [])
    produtos_atendidos = []
    produtos_nao_atendidos = []

    for pedido in pedidos:
        produto = Alimentos.objects.get(nome=pedido['produto'])
        quantidade_pedido = int(pedido['quantidade'])



    if quantidade_pedido <= produto.quantidade:
        produtos_atendidos.append((produto, quantidade_pedido))
    else:
        produtos_nao_atendidos.append((produto,quantidade_pedido))

    if produtos_nao_atendidos:
        for produto,quantidade_pedido in produtos_nao_atendidos:
            erro = f'Não há estoque disponivel para o produto {produto.nome}'
            context = {'erro':erro, 'produto':produto, 'quantidade':quantidade_pedido}
            return render(request, 'resultado_nao_esperado.html', context)

    total = 0
    for produto, quantidade_pedido in produtos_atendidos:
        total += produto.preco * quantidade_pedido
        produto.quantidade -= quantidade_pedido
        produto.save()

    del request.session['pedidos']

    contexto = {'pedidos':pedidos, 'total':total}
    return render(request, 'finalizar_pedido.html', contexto)
def tela_de_pagamento(request):
    return render(request, 'tela_de_pagamento.html')

def processar_pagamento(request):
    if request.method == 'POST':
        metodo_pagamento = request.POST.get('metodo_pagamento')
        if metodo_pagamento == 'cartao':
            return redirect('app_produtos:pagar_com_cartao')

        elif metodo_pagamento == 'pix':
            return redirect('app_produtos:pagar_com_pix')

        elif metodo_pagamento == 'dinheiro':
            return redirect('app_produtos:pagar_com_dinheiro')


    return redirect('app_produtos:pagina_de_erro.html')
def pagar_com_cartao(request):
    if request.method == 'POST':
        numero_cartao = request.POST.get('numero_cartao')
    return render(request, 'pagar_com_cartao.html')

def pagar_com_dinheiro(request):
    return render(request, 'pagar_com_dinheiro.html')
def pagar_com_pix(request):
    return render(request, 'pagar_com_pix.html')

def pagina_de_erro(request):
    return render(request, 'pagina_de_erro.html')


