from django.urls import path
from inicio.views import inicio,ingresar,adoptar,ingreso_exitoso,adopcion_exitosa,adopcion_fallida

urlpatterns=[
    path('', inicio, name='inicio'),
    path('ingresar/', ingresar, name='ingresar'),
    path('adoptar/', adoptar, name='adoptar'),
    path('ingreso-exitoso/', ingreso_exitoso, name='ingreso_exitoso'),
    path('adopcion-exitosa/', adopcion_exitosa, name='adopcion_exitosa'),
    path('adopcion-fallida/', adopcion_fallida, name='adopcion_fallida')
    ]
    