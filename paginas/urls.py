from django.urls import path
from . import views

urlpatterns = [
    path("buscar/<codserie>", views.buscar_serie, name="BuscarSerie"),
]
