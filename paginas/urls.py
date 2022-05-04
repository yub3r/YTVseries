from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioPaginas"),
    path("buscar/<codserie>", views.buscar_serie, name="BuscarSerie"),
    path("buscar/resultados", views.inicio, name="InicioPaginas"),
]
