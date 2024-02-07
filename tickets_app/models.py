from django.db import models
from concerts_app.models import Concierto
from users_app.models import Cliente
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


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
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def actualizarReservaYaExistente(self, unidades, importeNuevo):
        self.cantidad_tickets += unidades
        self.importe += importeNuevo
        self.save()

    def __str__(self):
        return f"{self.cliente_reserva} - {self.concierto_reserva} - {self.cantidad_tickets}"


"""
class Promocion(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    descuento = models.FloatField(default=0)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=timezone.now() + timezone.timedelta(days=15))

    def __str__(self):
        return self.nombre

    def calcularDescuento(self, importe):
        self.descuento = importe * 0.1
        self.save()
        return self.descuento

    class Meta:
        verbose_name_plural = "Promociones"
"""
