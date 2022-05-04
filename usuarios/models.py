from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    alias = models.CharField(max_length=25)

class Critico(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    alias = models.CharField(max_length=25)
    experiencia = models.TextField()

