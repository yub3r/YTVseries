from urllib import request
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse

from usuarios.models import Critico
from .forms import FormCritico


def inicio(request):
    return render(request, "usuarios/inicio.html")


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
            return redirect("InicioUsuarios")

    mi_form = FormCritico()

    return render(request, "usuarios/formCriticos.html", {"form": mi_form})
