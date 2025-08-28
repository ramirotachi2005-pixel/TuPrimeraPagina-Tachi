from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.forms import formulario_ingreso,formulario_adopcion
from inicio.models import Animal

def inicio(request):
    return render(request,'inicio/inicio.html')

def ingresar(request):
    
    if request.method == "POST":
        formulario = formulario_ingreso(request.POST)
        if formulario.is_valid():
            especie_nueva = formulario.cleaned_data.get('Especie')
            sexo_nueva = formulario.cleaned_data.get('Sexo')
            raza_nueva = formulario.cleaned_data.get('Raza')
            color_nueva = formulario.cleaned_data.get('Color')
            peso_nueva = formulario.cleaned_data.get('Peso')
            
    
            animal = Animal(Especie=especie_nueva,Sexo=sexo_nueva,Raza=raza_nueva,Color=color_nueva,Peso=peso_nueva)
            animal.save()
            return redirect('ingreso_exitoso')
    else:
        formulario = formulario_ingreso()
    
    return render(request, 'inicio/ingresar.html',{'formulario':formulario})

def ingreso_exitoso(request):
    return render(request,'inicio/ingreso_exitoso.html')

def adoptar(request):
    
    if request.method == "POST":
        formulario = formulario_ingreso(request.POST)
        if formulario.is_valid():
            especie_nueva = formulario.cleaned_data.get('Especie')
            sexo_nueva = formulario.cleaned_data.get('Sexo')
            raza_nueva = formulario.cleaned_data.get('Raza')
            color_nueva = formulario.cleaned_data.get('Color')
            peso_nueva = formulario.cleaned_data.get('Peso')
            
            animales = Animal.objects.all()
            encontrado = False
            for animal in animales:
               if (
                   animal.Especie.lower() == especie_nueva.lower() and
                    animal.Sexo.lower() == sexo_nueva.lower() and
                    animal.Raza.lower() == raza_nueva.lower() and
                    animal.Color.lower() == color_nueva.lower() and
                    animal.Peso == peso_nueva
               ):
                   encontrado = True
                   break
            if encontrado == True :
                animal.delete()
                return redirect('adopcion_exitosa')
                
            else:
                return redirect('adopcion_fallida')
    
    else:
        
        formulario = formulario_adopcion()
        animales = Animal.objects.all()
        return render(request, 'inicio/adoptar.html',{'formulario':formulario, 'listado_de_animales': animales})

def adopcion_exitosa(request):
    return render(request,'inicio/adopcion_exitosa.html')

def adopcion_fallida(request):
    return render(request,'inicio/adopcion_fallida.html')


# Create your views here.
