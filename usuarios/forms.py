#from tkinter import Widget
from django import forms


class FormCritico(forms.Form):
    nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    email = forms.EmailField()
    alias = forms.CharField(max_length=25)
    experiencia = forms.CharField(widget=forms.Textarea)


class FormUsuario(forms.Form):
    nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    email = forms.EmailField()
    alias = forms.CharField(max_length=25)
    