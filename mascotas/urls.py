from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"mascota", views.MascotaViewSet)
router.register(r"adoptante", views.AdoptanteViewSet)
router.register(r"adopcion", views.AdopcionViewSet)
router.register(r"vacuna", views.VacunaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
