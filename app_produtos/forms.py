from django import forms
from .models import Alimentos

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nome', 'quantidade', 'preco']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nome', 'quantidade']
