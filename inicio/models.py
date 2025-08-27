from django.db import models

class Animal(models.Model):
    Especie = models.CharField(max_length=25)
    Sexo = models.CharField(max_length=10)
    Raza = models.CharField(max_length=25)
    Color = models.CharField(max_length=20)
    Peso = models.CharField(max_length=6)
