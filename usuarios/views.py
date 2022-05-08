from urllib import request
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse

from usuarios.models import Critico, Usuario
from .forms import FormCritico


def inicio(request):
    return render(request, "usuarios/inicio.html")


def criticos(request):
    critico = Critico.objects.all()
    # usuario = Usuario.objects.all()
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
            
            critic.nombre=info["nombre"]
            critic.apellido=info["apellido"]
            critic.email=info["email"]
            critic.alias=info["alias"]
            critic.experiencia=info["experiencia"]
        
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

    return render(request, "usuarios/formCriticos.html", {"form": mi_form})


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

    return render(request, "usuarios/formCriticos.html", {"form": mi_form})



def del_critico(request, id):
    critic = Critico.objects.get(id=id)

    critic.delete()
    return redirect("ListaCriticos")