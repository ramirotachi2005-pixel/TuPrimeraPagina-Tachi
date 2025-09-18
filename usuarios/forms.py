from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms



class Registro(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        help_texts = {llave: '' for llave in fields}

class Iniciar_sesion(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {llave: '' for llave in fields}
    
class Editar_perfil(UserChangeForm):
    password = None
    username = forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")    
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        help_texts = {llave: '' for llave in fields}
