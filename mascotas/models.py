from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from voluntarios.models import Voluntario

# Create your models here.

class Especies(models.TextChoices):
    perro = 'p', 'Perro'
    gato = 'g', 'Gato'
    otro = 'o', 'Otro'

class Genero(models.TextChoices):
    MACHO = 'm', 'Macho'
    HEMBRA = 'h', 'Hembra'

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(
        max_length=1,
        choices=Especies.choices,
        default=Especies.perro
    )
    edad = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=1,
        choices=Genero.choices,
        default=Genero.MACHO
    )
    fecha_ingreso = models.DateTimeField()
    lugar_rescate = models.TextField()
    voluntario = models.ForeignKey(Voluntario, related_name='mascotas', on_delete=models.SET_NULL, null=True, blank=True)
    para_adopcion = models.BooleanField(default=False)

    def clean(self):
        if not self.edad:
            raise ValidationError(_('La edad es obligatoria.'))
        if not self.nombre:
            raise ValidationError(_('El nombre es obligatorio.'))

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class Adoptante(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def clean(self):
        if not self.direccion:
            raise ValidationError(_('La direccion es obligatoria.'))
        if not self.telefono:
            raise ValidationError(_('El telefono es obligatorio.'))
        if not self.telefono.isdigit():
            raise ValidationError('El teléfono debe contener solo números')

    def __str__(self):
        return self.nombre
    
class Adopcion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    fecha_adopcion = models.DateField()

    def __str__(self):
        return f"Adopción de {self.mascota} por {self.adoptante}"

class Vacuna(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    nombre_vacuna = models.CharField(max_length=100)
    fecha_vacunacion = models.DateField()
    lugar_vacunacion = models.TextField()
    doctor = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre_vacuna} para {self.mascota}"