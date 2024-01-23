from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Cliente(AbstractUser):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.PositiveIntegerField()
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
