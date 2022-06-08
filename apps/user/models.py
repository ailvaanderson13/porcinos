from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.company.models import Company


class User(AbstractUser):
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, null=True, blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True, default='000.000.000-00')
    telefone = models.CharField(max_length=15, blank=True, null=True)
    empresa = models.BooleanField(default=False)
    loja = models.BooleanField(default=False)
    client = models.BooleanField(default=False)
    categoria = models.BooleanField(default=False)
    produto = models.BooleanField(default=False)
    deleta_pedidos = models.BooleanField(default=False)
    historico_pedidos = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.first_name} - {self.email}"

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['data']
