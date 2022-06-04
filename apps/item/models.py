from django.db import models
from apps.categoria.models import Category
from apps.company.models import Company


class Item(models.Model):
    categoria = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField(blank=True, null=True)
    valor_custo = models.FloatField(max_length=10, blank=True, null=True)
    valor_venda = models.FloatField(max_length=10, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    code_bar = models.CharField(max_length=20, blank=True, null=True)
    descricao = models.TextField(max_length=200, blank=True, null=True)
    empty = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
