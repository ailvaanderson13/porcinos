from django.db import models
from apps.user.models import User


class Cliente(User):
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
