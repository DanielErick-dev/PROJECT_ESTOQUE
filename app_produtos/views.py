from django.shortcuts import render
from .models import Alimentos

def exibir_alimentos(request):
    alimentos = Alimentos.objects.all()


    dicionario_alimentos = {
        'alimentos': alimentos
    }


    return render(request, 'index.html', dicionario_alimentos)

