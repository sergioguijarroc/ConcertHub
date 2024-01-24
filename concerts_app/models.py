from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class Concierto(models.Model):
    nombre = models.CharField(max_length=255)
    artista_concierto = models.ForeignKey(Artista, on_delete=models.CASCADE)
    ubicacion_concierto = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    boletos_disponibles = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.artista} - {self.fecha}"


class Review(models.Model):
    concierto = models.ForeignKey(Concierto, on_delete=models.CASCADE)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.TextField()

    def __str__(self):
        return f"{self.cliente} - {self.concierto} - Calificación: {self.calificacion}"


class Notificacion(models.Model):
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    mensaje = models.TextField()

    def __str__(self):
        return f"Notificación para {self.cliente}: {self.mensaje}"


class Cliente(AbstractUser):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.PositiveIntegerField()
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
