from django.urls import path
from .views import exibir_estoque, exibir_pagina_inicial

app_name = 'app_produtos'
urlpatterns = [
    path('', exibir_pagina_inicial, name='exibir_pagina_inicial'),
    path('exibir_estoque', exibir_estoque, name='exibir_estoque'),
]