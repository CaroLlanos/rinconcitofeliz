from rest_framework import serializers
from .models import MascotaPerdida

class MascotaPerdidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MascotaPerdida
        fields = '__all__'