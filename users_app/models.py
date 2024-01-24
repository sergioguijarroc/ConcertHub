from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Cliente(AbstractUser):
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=255)
    direccion = models.TextField()

    # Añadir un campo de dinero gastado, cuando sea más de X, ponerle en un tier bronce,plata,oro y que tengan descuentos.
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Staff(AbstractUser):
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
