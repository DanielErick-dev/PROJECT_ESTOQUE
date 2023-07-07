from django.shortcuts import render
from .models import Alimentos

def exibir_alimentos(request):
    alimentos = Alimentos.objects.all()
    return render(request, 'index.html', {'alimentos': alimentos})

