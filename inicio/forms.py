from django import forms

class formulario_ingreso(forms.Form):
    Especie = forms.CharField(max_length=25)
    Sexo = forms.CharField(max_length=10)
    Raza = forms.CharField(max_length=25)
    Color = forms.CharField(max_length=25)
    Peso = forms.CharField(max_length=6)
    
class formulario_adopcion(forms.Form):
    Especie = forms.CharField(max_length=25)
    Sexo = forms.CharField(max_length=10)
    Raza = forms.CharField(max_length=25)
    Color = forms.CharField(max_length=25)
    Peso = forms.CharField(max_length=6)