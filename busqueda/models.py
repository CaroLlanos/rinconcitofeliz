from django.db import models

# Create your models here.

class MascotaPerdida(models.Model):
    nombre_mascota = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_perdida = models.DateField()
    nombre_propietario = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)
