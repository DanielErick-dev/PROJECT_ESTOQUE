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

class PagamentoForm(forms.ModelForm):
    class Meta:
        numero_cartao = forms.CharField(label='numero_do_cartao', widget=forms.TextInput(attrs={'placeholder':'insira o número do cartão de crédito'}))
