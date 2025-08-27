from django.shortcuts import render
from django.http import HttpResponse
from inicio.forms import formulario_ingreso,formulario_adopcion


def inicio(request):
    return render(request,'inicio/inicio.html')

def ingresar(request):
    
    formulario = formulario_ingreso()
    
    return render(request, 'inicio/ingresar.html',{'formulario':formulario})

def adoptar(request):
    formulario = formulario_adopcion()
    return render(request, 'inicio/adoptar.html',{'formulario':formulario})

# Create your views here.
