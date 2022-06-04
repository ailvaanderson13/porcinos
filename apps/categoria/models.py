from django.db import models
from apps.company.models import Company


class Category(models.Model):
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, null=True, blank=True)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'