from rest_framework import serializers
from .models import Voluntario

class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        fields = '__all__'