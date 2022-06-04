from tabnanny import verbose
from django.db import models


class Company(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    rua = models.CharField(max_length=255)
    numero_endereco = models.CharField(max_length=10)
    cep = models.CharField(max_length=9)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=15)
    data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name="Empresa"
        verbose_name_plural="Empresas"

