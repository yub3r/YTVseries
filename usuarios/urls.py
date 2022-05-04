from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioUsuarios"),
    path("nuevo_critico", views.nuevo_critico, name="NuevoCritico"),
]
