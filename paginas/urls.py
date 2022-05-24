from django.urls import path
from . import views

urlpatterns = [
    path("buscarserie", views.buscarSerie, name="BuscarSerie"),
    path("buscar/", views.buscarS, name="BuscarS"),
    path("series", views.serie, name="ListaSeries"),
    path("serie/<codserie>", views.ver_serie, name="VerSerie"),
    path("nueva_serie", views.nueva_serie, name="NuevaSerie"),
    path("login", views.login, name="Login"),
    
]
