from django.db import models

class Animal(models.Model):
    Especie = models.CharField(max_length=25)
    Sexo = models.CharField(max_length=10)
    Raza = models.CharField(max_length=25)
    Color = models.CharField(max_length=25)
    Peso = models.CharField(max_length=10)
    Edad = models.CharField(max_length=20)
    Info = models.CharField(max_length=300, blank=True)
    imagen = models.ImageField(upload_to='animales', blank=True, null=True)

    
    def __str__(self):
        return f"{self.Especie} - {self.Raza} - {self.Edad}"
    
    # def __repr__(self):
        # return f"Marca: {self.Especie} {self.Sexo} {self.Raza} {self.Color} {self.Peso}"