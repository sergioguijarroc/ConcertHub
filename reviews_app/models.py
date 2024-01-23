from django.db import models
from concerts_app.models import Concierto
from users_app.models import Cliente
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    concierto = models.ForeignKey(Concierto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.TextField()

    def __str__(self):
        return f"{self.cliente} - {self.concierto} - Calificación: {self.calificacion}"
