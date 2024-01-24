from django.db import models
from concerts_app.models import Concierto
from users_app.models import Cliente
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Reserva(models.Model):
    concierto_reserva = models.ForeignKey(Concierto, on_delete=models.CASCADE)
    cliente_reserva = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    cantidad_tickets = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]  # Como máximo puede comprar 5 boletos
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente} - {self.concierto} - {self.cantidad_tickets}"
