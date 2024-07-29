from django.shortcuts import render
from rest_framework import viewsets
from .models import MascotaPerdida
from .serializers import MascotaPerdidaSerializer

# Create your views here.

class MascotaPerdidaViewSet(viewsets.ModelViewSet):
    queryset = MascotaPerdida.all()
    serializer_class = MascotaPerdidaSerializer