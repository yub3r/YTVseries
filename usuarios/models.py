from email.policy import default
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    alias = models.CharField(max_length=25)

    def __str__(self):
        return f"Usuario {self.nombre} {self.apellido}"


class Critico(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    alias = models.CharField(max_length=25)
    experiencia = models.TextField()

    def __str__(self):
        return f"Critico {self.nombre} {self.apellido}"