from django import forms
from .models import Alimentos, RemoverAlimentos

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nome', 'quantidade', 'preco']
        labels = {'nome': 'nome'.upper(),
                 'quantidade': 'quantidade'.upper(),
                 'preco': 'preço'.upper()}

class RemoverAlimentoForm(forms.ModelForm):
    class Meta:
        model = RemoverAlimentos
        fields = ['nome']
        labels = {'nome'.upper(): 'Nome do Alimento a Remover'}
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nome', 'quantidade']

class PagamentoForm(forms.ModelForm):
    class Meta:
        numero_cartao = forms.CharField(label='numero_do_cartao', widget=forms.TextInput(attrs={'placeholder':'insira o número do cartão de crédito'}))
