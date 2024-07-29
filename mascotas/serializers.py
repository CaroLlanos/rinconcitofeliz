from rest_framework import serializers
from .models import Mascota, Adoptante, Adopcion, Vacuna

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

class AdoptanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoptante
        fields = '__all__'

class AdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopcion
        fields = '__all__'

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = '__all__'