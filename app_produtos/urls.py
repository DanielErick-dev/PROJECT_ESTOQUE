from django.urls import path
from .views import exibir_estoque, exibir_pagina_inicial, adicionar_alimento

app_name = 'app_produtos'
urlpatterns = [
    path('', exibir_pagina_inicial, name='exibir_pagina_inicial'),
    path('exibir_estoque', exibir_estoque, name='exibir_estoque'),
    path('adicionar_alimento', adicionar_alimento, name='adicionar_alimento')
]