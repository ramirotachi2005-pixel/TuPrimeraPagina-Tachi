from django import forms

class formulario_ingreso(forms.Form):
    Especie = forms.CharField(max_length=25)
    Sexo = forms.CharField(max_length=10)
    Raza = forms.CharField(max_length=25)
    Color = forms.CharField(max_length=25)
    Peso = forms.CharField(max_length=10)
    Edad = forms.CharField(max_length=20)
    Info = forms.CharField(max_length=300,required=False, widget=forms.Textarea(attrs={
        'style': 'width:350px; height:125px; padding:5px; line-height:1.2; verbose_name="Infoadicional"; font-size:14px;',
        'wrap': 'soft',
        }))
    imagen = forms.ImageField(required=False)
    
class formulario_adopcion(forms.Form):
    Especie = forms.CharField(max_length=25)
    Sexo = forms.CharField(max_length=10)
    Raza = forms.CharField(max_length=25)
    Color = forms.CharField(max_length=25)
    Peso = forms.CharField(max_length=10)
    Edad = forms.CharField(max_length=20)
