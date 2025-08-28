from django.db import models

class Animal(models.Model):
    Especie = models.CharField(max_length=25)
    Sexo = models.CharField(max_length=10)
    Raza = models.CharField(max_length=25)
    Color = models.CharField(max_length=25)
    Peso = models.CharField(max_length=6)
    
    #def __str__(self):
    #    return 
    
    def __repr__(self):
        return f"Marca: {self.Especie} {self.Sexo} {self.Raza} {self.Color} {self.Peso}"