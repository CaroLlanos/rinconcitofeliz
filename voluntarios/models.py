from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Voluntario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    edad = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

    def clean(self):
        if not self.telefono.isdigit():
            raise ValidationError('El teléfono debe contener solo números')
        if not self.edad:
            raise ValidationError(_('La edad es obligatoria.'))
        if not self.direccion:
            raise ValidationError(_('La direccion es obligatoria.'))