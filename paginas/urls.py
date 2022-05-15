from django.urls import path
from . import views

urlpatterns = [
    path("buscar/<codserie>", views.buscar_serie, name="BuscarSerie"),
    path("series", views.serie, name="ListaSeries"),
    path("serie/<nombre>", views.ver_serie, name="VerSerie"),
    path("nueva_serie", views.nueva_serie, name="NuevaSerie"),
    

]
