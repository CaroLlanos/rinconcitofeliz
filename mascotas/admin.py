from django.contrib import admin
from .models import Mascota
from .models import Vacuna
from .models import Adopcion
from .models import Adoptante

# Register your models here.

"""
Mascota
"""
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "edad", "color", "para_adopcion",)
    search_fields = ["nombre"]
    list_filter = ("para_adopcion",)

admin.site.register(Mascota, MascotaAdmin)

