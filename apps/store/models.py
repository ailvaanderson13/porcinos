from django.db import models
from apps.company.models import Company

class Store(models.Model):
    empresa = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    id_store = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
