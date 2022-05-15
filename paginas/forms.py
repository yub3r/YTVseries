from tkinter import Widget
from django import forms


class FormSerie(forms.Form):
    nombre = forms.CharField(max_length=255)
    tipo = forms.CharField(max_length=255)
    plataforma = forms.CharField(max_length=255)
    fecha = forms.DateField()
    episodio = forms.IntegerField()
    temporada = forms.IntegerField()
    terminada = forms.BooleanField()
    sinopsis = forms.CharField(widget=forms.Textarea)
    codserie = forms.CharField(max_length=25)

