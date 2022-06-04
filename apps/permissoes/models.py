from django.db import models
from apps.company.models import Company


class Perfil(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(to=Company, on_delete=models.DO_NOTHING, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    criar_usuario = models.BooleanField(default=False, blank=True)
    editar_usuario = models.BooleanField(default=False, blank=True)
    excluir_usuario = models.BooleanField(default=False, blank=True)
    ver_usuario = models.BooleanField(default=False, blank=True)
    #
    criar_categoria = models.BooleanField(default=False, blank=True)
    editar_categoria = models.BooleanField(default=False, blank=True)
    excluir_categoria = models.BooleanField(default=False, blank=True)
    ver_categoria = models.BooleanField(default=False, blank=True)
    #
    criar_produto = models.BooleanField(default=False, blank=True)
    editar_produto = models.BooleanField(default=False, blank=True)
    excluir_produto = models.BooleanField(default=False, blank=True)
    ver_produto = models.BooleanField(default=False, blank=True)
    #
    criar_pedido = models.BooleanField(default=False, blank=True)
    editar_pedido = models.BooleanField(default=False, blank=True)
    excluir_pedido = models.BooleanField(default=False, blank=True)
    ver_pedido = models.BooleanField(default=False, blank=True)
    #
    criar_empresa = models.BooleanField(default=False, blank=True)
    editar_empresa = models.BooleanField(default=False, blank=True)
    excluir_empresa = models.BooleanField(default=False, blank=True)
    ver_empresa = models.BooleanField(default=False, blank=True)
    #
    criar_perfil = models.BooleanField(default=False, blank=True)
    editar_perfil = models.BooleanField(default=False, blank=True)
    excluir_perfil = models.BooleanField(default=False, blank=True)
    ver_perfil = models.BooleanField(default=False, blank=True)
    #
    is_active = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.company if self.company else 'Nenhuma'}"
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
