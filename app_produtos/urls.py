from django.urls import path
from .views import exibir_alimentos

app_name = 'app_produtos'
urlpatterns = [
    path('', exibir_alimentos, name='exibir_alimentos')
]