from django.urls import path
from .views import exibir_estoque, exibir_pagina_inicial, adicionar_alimento,\
                   exibir_produtos_venda, processar_resposta, resultado_nao_esperado, adicionar_pedido,\
    finalizar_pedido




app_name = 'app_produtos'
urlpatterns = [
    path('', exibir_pagina_inicial, name='exibir_pagina_inicial'),
    path('exibir_estoque', exibir_estoque, name='exibir_estoque'),
    path('adicionar_alimento', adicionar_alimento, name='adicionar_alimento'),
    path('exibir_produtos_venda', exibir_produtos_venda, name='exibir_produtos_venda'),
    path('processar_resposta', processar_resposta, name='processar_resposta'),
    path('resultado_nao_esperado', resultado_nao_esperado, name='resultado_nao_esperado'),
    path('adicionar_pedido', adicionar_pedido, name='adicionar_pedido'),
    path('finalizar_pedido', finalizar_pedido, name='finalizar_pedido')
]
