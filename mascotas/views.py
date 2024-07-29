from django.shortcuts import render
from rest_framework import viewsets
from .models import Mascota, Adoptante, Adopcion, Vacuna
from .serializers import MascotaSerializer, AdoptanteSerializer, AdopcionSerializer, VacunaSerializer

# Create your views here.

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class AdoptanteViewSet(viewsets.ModelViewSet):
    queryset = Adoptante.objects.all()
    serializer_class = AdoptanteSerializer

class AdopcionViewSet(viewsets.ModelViewSet):
    queryset = Adopcion.objects.all()
    serializer_class = AdopcionSerializer

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer
