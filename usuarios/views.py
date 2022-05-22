from urllib import request
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from platformdirs import user_cache_dir

from usuarios.models import Critico, Usuario
from .forms import FormCritico, FormUsuario


def inicio(request):
    return render(request, "usuarios/inicio.html")


def usuarios(request):
    user = Usuario.objects.all()
    return render(request, "usuarios/users.html", {"usuarios": user})


def ver_usuarios(request, nombre):
    user = Usuario.objects.get(nombre=nombre)
    return render(request, "usuarios/ver_user.html", {"usuario": user})


def nuevo_usuario(request):
    if request.method == "POST":
        mi_form = FormUsuario(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            user = Usuario(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                alias=info["alias"],
            )
            user.save()
            return redirect("ListaUsuarios")

    mi_form = FormUsuario()

    return render(request, "usuarios/formUsuarios.html", {"Userform": mi_form})


def mod_usuario(request, id):
    user = Usuario.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormUsuario(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            user.nombre = info["nombre"]
            user.apellido = info["apellido"]
            user.email = info["email"]
            user.alias = info["alias"]

            user.save()
            return redirect("ListaUsuarios")

    mi_form = FormUsuario(
        initial={
            "nombre": user.nombre,
            "apellido": user.apellido,
            "email": user.email,
            "alias": user.alias,
        }
    )

    return render(request, "usuarios/formUsuarios.html", {"Userform": mi_form})


def del_usuario(request, id):
    user = Usuario.objects.get(id=id)

    user.delete()
    return redirect("ListaUsuarios")



def buscarUsuario(request):
    return render(request, "usuarios/buscarUsuario.html")
    #return redirect("BuscarUsuario")

def buscarU(request):
    if request.GET.get("nombre"):                                           
        nombre = request.GET.get("nombre")                                 
        user = Usuario.objects.filter(nombre__icontains=nombre)                            
        return render(request, "usuarios/busquedaU.html", {"user": user}) 

    return render(request, "usuarios/buscarUsuario.html")


def criticos(request):
    critico = Critico.objects.all()

    return render(request, "usuarios/criticos.html", {"criticos": critico})


def ver_critico(request, nombre):
    critic = Critico.objects.get(nombre=nombre)
    return render(request, "usuarios/ver_critico.html", {"critico": critic})


def mod_critico(request, id):
    critic = Critico.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormCritico(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            critic.nombre = info["nombre"]
            critic.apellido = info["apellido"]
            critic.email = info["email"]
            critic.alias = info["alias"]
            critic.experiencia = info["experiencia"]

            critic.save()
            return redirect("ListaCriticos")

    mi_form = FormCritico(
        initial={
            "nombre": critic.nombre,
            "apellido": critic.apellido,
            "email": critic.email,
            "alias": critic.alias,
            "experiencia": critic.experiencia,
        }
    )

    return render(request, "usuarios/formCriticos.html", {"Criticform": mi_form})


def nuevo_critico(request):
    if request.method == "POST":
        mi_form = FormCritico(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            critic = Critico(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                alias=info["alias"],
                experiencia=info["experiencia"],
            )
            critic.save()
            return redirect("ListaCriticos")

    mi_form = FormCritico()

    return render(request, "usuarios/formCriticos.html", {"Criticform": mi_form})


def del_critico(request, id):
    critic = Critico.objects.get(id=id)

    critic.delete()
    return redirect("ListaCriticos")
