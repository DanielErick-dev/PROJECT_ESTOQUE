from django.db import models


class Alimentos(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)


class RemoverAlimentos(models.Model):
    nome = models.CharField(max_length=100)