from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from usuarios.forms import Registro, Iniciar_sesion, Editar_perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def iniciar_sesion(request):
    
    if request.method == "POST":
        formulario = Iniciar_sesion(request, data=request.POST)
        if formulario.is_valid():
             usuario = formulario.get_user()
             
             login(request, usuario)
             
             return redirect('inicio')
    else:
        formulario = Iniciar_sesion()
    
    return render(request,'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registro(request):
    
    if request.method == "POST":
        formulario = Registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect("iniciar_sesion")
    else:
        formulario = Registro()
        
    return render(request, 'usuarios/registro.html', {'formulario':formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {'user': request.user})

@login_required
def editar_perfil(request):
    
    if request.method == "POST":
        formulario = Editar_perfil(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')
    else:    
        formulario = Editar_perfil(instance=request.user)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario':formulario})


class editar_contrasenia(PasswordChangeView):
    template_name = 'usuarios/editar_contrasenia.html'
    success_url = reverse_lazy('perfil')



