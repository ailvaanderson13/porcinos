from django.db import models
from apps.cliente.models import Cliente
from apps.store.models import Store
from apps.item.models import Item
from apps.user.models import User
from . import choices


class Pedido(models.Model):
    codigo = models.CharField(max_length=15)
    cliente = models.ForeignKey(to=Cliente, on_delete=models.DO_NOTHING, blank=True, null=True)
    item = models.ManyToManyField(to=Item, blank=True, null=True)
    loja = models.ForeignKey(to=Store, on_delete=models.DO_NOTHING, blank=True, null=True)
    detalhes = models.CharField(max_length=255, blank=True, null=True)
    forma_pag = models.CharField(choices=choices.FORMA_PAGAMENTO_CHOICES, default='0', max_length=3)
    obs = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.cliente.first_name}"

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
