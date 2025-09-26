from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.forms import formulario_ingreso,formulario_adopcion
from inicio.models import Animal
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test

def superusuario_required(user):
    return user.is_superuser

def acceso_denegado(request):
    return render(request, 'inicio/acceso_denegado.html')

def inicio(request):
    return render(request,'inicio/inicio.html')

@user_passes_test(superusuario_required, login_url='acceso_denegado')
def ingresar(request):
    
    if request.method == "POST":
        formulario = formulario_ingreso(request.POST, request.FILES)
        if formulario.is_valid():
            especie_nueva = formulario.cleaned_data.get('Especie')
            sexo_nueva = formulario.cleaned_data.get('Sexo')
            raza_nueva = formulario.cleaned_data.get('Raza')
            color_nueva = formulario.cleaned_data.get('Color')
            peso_nueva = formulario.cleaned_data.get('Peso')
            edad_nueva = formulario.cleaned_data.get('Edad')
            info_nueva = formulario.cleaned_data.get('Info')
            imagen_nueva = formulario.cleaned_data.get('imagen')
            
    
            animal = Animal(Especie=especie_nueva,Sexo=sexo_nueva,Raza=raza_nueva,Color=color_nueva,Peso=peso_nueva,Edad=edad_nueva,Info=info_nueva,imagen=imagen_nueva)
            animal.save()
            return redirect('ingreso_exitoso')
    else:
        formulario = formulario_ingreso()
    
    return render(request, 'inicio/ingresar.html',{'formulario':formulario})

@login_required
def ingreso_exitoso(request):
    return render(request,'inicio/ingreso_exitoso.html')

@login_required
def adoptar(request):
    
    if request.method == "POST":
        formulario = formulario_adopcion(request.POST)
        
        
        
        if formulario.is_valid():
            especie_nueva = formulario.cleaned_data.get('Especie')
            sexo_nueva = formulario.cleaned_data.get('Sexo')
            raza_nueva = formulario.cleaned_data.get('Raza')
            color_nueva = formulario.cleaned_data.get('Color')
            peso_nueva = formulario.cleaned_data.get('Peso')
            edad_nueva = formulario.cleaned_data.get('Edad')
            
            animales = Animal.objects.all()
            encontrado = False
            for animal in animales:
               if (
                   animal.Especie.lower() == especie_nueva.lower() and
                    animal.Sexo.lower() == sexo_nueva.lower() and
                    animal.Raza.lower() == raza_nueva.lower() and
                    animal.Color.lower() == color_nueva.lower() and
                    animal.Peso.lower() == peso_nueva.lower() and
                    animal.Edad.lower() == edad_nueva.lower()
               ):
                   encontrado = True
                   break
            if encontrado == True :
                animal.delete()
                origen = "adoptar"
                return redirect(f'/adopcion-exitosa/?origen={origen}&animal_id={animal.id}')
                
            else:
                return redirect('adopcion_fallida')

    
    else:
        
        formulario = formulario_adopcion()
        animales = Animal.objects.all()
        return render(request, 'inicio/adoptar.html',{'formulario':formulario, 'listado_de_animales': animales})

def adopcion_exitosa(request):
    origen = request.GET.get("origen")
    animal_id = request.GET.get("animal_id")
    return render(request,'inicio/adopcion_exitosa.html', {"origen": origen, "animal_id": animal_id})

def adopcion_fallida(request):
    return render(request,'inicio/adopcion_fallida.html')

@login_required
def actualizar_borrar(request):
    animales = Animal.objects.all()
    
    return render(request, 'inicio/actualizar_borrar.html', {'animales': animales})

@login_required
def detalle(request, animal_id):
    
    animal = Animal.objects.get(id=animal_id)
    
    if request.method == "POST":  # 👈 SOLO si fue un POST
        animal.delete()
        origen = "detalle"
        return redirect(f'/adopcion-exitosa/?origen={origen}&animal_id={animal_id}')
    
    return render (request, 'inicio/detalle.html', {'animal':animal})


class actualizar(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Animal
    template_name = "inicio/actualizar.html"
    fields = "__all__"
    success_url = reverse_lazy('actualizar_borrar')
    
    def test_func(self):
        return self.request.user.is_superuser

    # Qué hacer si no pasa la prueba (redireccionar a tu vista)
    def handle_no_permission(self):
        return redirect('acceso_denegado')
    
    
class borrar(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Animal
    template_name = "inicio/borrar.html"
    success_url = reverse_lazy('actualizar_borrar')
    
    def test_func(self):
        return self.request.user.is_superuser

    # Qué hacer si no pasa la prueba (redireccionar a tu vista)
    def handle_no_permission(self):
        return redirect('acceso_denegado')



