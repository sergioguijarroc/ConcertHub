from django.db import models


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
