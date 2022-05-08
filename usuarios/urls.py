from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioUsuarios"),
    path("criticos", views.criticos, name="ListaCriticos"),
    path("nuevo_critico", views.nuevo_critico, name="NuevoCritico"),
    path("critico/<nombre>", views.ver_critico, name="VerCritico"),
    path("critico/editar/<id>", views.mod_critico, name="EditarCritico"),
    path("critico/eliminar/<id>", views.del_critico, name="EliminarCritico"),
]
