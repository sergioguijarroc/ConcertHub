from django.db import models
from users_app.models import Cliente

# Create your models here.


class Notificacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mensaje = models.TextField()

    def __str__(self):
        return f"Notificación para {self.cliente}: {self.mensaje}"
