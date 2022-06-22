from django.db import models
from apps.user.models import User
from apps.store.models import Store
from apps.item.models import Item
from . import choices


class Pedido(models.Model):
    codigo = models.CharField(max_length=15)
    usuario = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, blank=True, null=True)
    item = models.ManyToManyField(to=Item, blank=True)
    loja = models.ForeignKey(to=Store, on_delete=models.DO_NOTHING, blank=True, null=True)
    detalhes = models.CharField(max_length=255, blank=True, null=True)
    dinheiro = models.BooleanField(default=False)
    pix = models.BooleanField(default=False)
    debito = models.BooleanField(default=False)
    credito = models.BooleanField(default=False)
    obs = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.usuario.first_name}"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
