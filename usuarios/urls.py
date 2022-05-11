from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioUsuarios"),
    path("criticos", views.criticos, name="ListaCriticos"),
    path("nuevo_critico", views.nuevo_critico, name="NuevoCritico"),
    path("critico/<nombre>", views.ver_critico, name="VerCritico"),
    path("critico/editar/<id>", views.mod_critico, name="EditarCritico"),
    path("critico/eliminar/<id>", views.del_critico, name="EliminarCritico"),
    path("usuarios", views.usuarios, name="ListaUsuarios"),
    path("nuevo_usuario", views.nuevo_usuario, name="NuevoUsuario"),
    path("user/<nombre>", views.ver_usuarios, name="VerUsuario"),
    path("user/editar/<id>", views.mod_usuario, name="EditarUsuario"),
    path("user/eliminar/<id>", views.del_usuario, name="EliminarUsuario"),
]