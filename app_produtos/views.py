from django.shortcuts import render, redirect, get_object_or_404
from .models import Alimentos
from .forms import AlimentoForm, PedidoForm, PagamentoForm, RemoverAlimentoForm
from django.http import Http404
from django.db import Error
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
    validacao_ok = request.session.get('validacao_ok', False)
    dicionario_alimentos = {
        'alimentos': ALIMENTOS, 'form': form, 'validacao_ok': validacao_ok
    }

    return render(request, 'vizualizar_estoque.html', dicionario_alimentos)


def adicionar_alimento(request):
    validacao_ok = False
    request.session.delete()
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            nome_produto = form.cleaned_data['nome']
            nome_produto = nome_produto.upper()

            alimento = form.save(commit=False)
            alimento.nome = nome_produto
            igualdade = False
            try:
                alimentos = Alimentos.objects.filter(nome=nome_produto)

                if len(alimentos) > 0:
                    igualdade = True
                    print('o produto em questão já existe no banco de dados')
                    print(validacao_ok)
            except Error:
                print('erro para acessar o banco de dados')

            if igualdade is False:
                alimento.save()
                print('novo objeto salvo no banco de dados')
                validacao_ok = True
                print(validacao_ok)

            request.session['validacao_ok'] = validacao_ok

            return redirect('app_produtos:exibir_estoque')

    else:
        form = AlimentoForm()
    validacao_ok = request.session.get('validacao_ok', False)

    return render(request, 'vizualizar_estoque.html', {'form': form, 'validacao_ok': validacao_ok})
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
    request.session.flush()


    return render(request, 'resultado_nao_esperado.html', {'mensagem': mensagem})

def adicionar_pedido(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        try:
            produto = get_object_or_404(Alimentos, id=produto_id)
            pedidos = request.session.get('pedidos', [])
            pedido_existente = False

            for pedido in pedidos:
                if pedido['produto'] == produto.nome:
                    pedido['quantidade'] += 1
                    pedido_existente = True
                    break
            if not pedido_existente:
                pedidos.append({'produto': produto.nome, 'quantidade': 1})
            request.session['pedidos'] = pedidos
        except Http404:
            return resultado_nao_esperado(request)

    return redirect('app_produtos:exibir_produtos_venda')

def finalizar_pedido(request):

    pedidos = request.session.get('pedidos', [])
    for pedido in pedidos:
        print(pedido['produto'])
    produtos_atendidos = []
    produtos_nao_atendidos = []
    total = 0
    for pedido in pedidos:
        produto = Alimentos.objects.get(nome=pedido['produto'])

        quantidade_pedido = int(pedido['quantidade'])

        if quantidade_pedido <= produto.quantidade:
            produtos_atendidos.append((produto, quantidade_pedido))
        else:
            produtos_nao_atendidos.append((produto,quantidade_pedido))

    if produtos_nao_atendidos:
        for produto, quantidade_pedido in produtos_nao_atendidos:
            erro = f'Não há estoque disponivel para o produto {produto.nome}'
            context = {'erro':erro, 'produto':produto, 'quantidade':quantidade_pedido}
            return render(request, 'resultado_nao_esperado.html', context)


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


