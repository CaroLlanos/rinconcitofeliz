from django.shortcuts import render
from rest_framework import viewsets
from .models import Voluntario
from .serializers import VoluntarioSerializer

# Create your views here.

class VoluntarioViewSet(viewsets.ModelViewSet):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer