from django.urls import path
from inicio.views import inicio,ingresar,adoptar,ingreso_exitoso,adopcion_exitosa,adopcion_fallida,actualizar_borrar,detalle,actualizar,borrar

urlpatterns=[
    path('', inicio, name='inicio'),
    path('ingresar/', ingresar, name='ingresar'),
    path('adoptar/', adoptar, name='adoptar'),
    path('ingreso-exitoso/', ingreso_exitoso, name='ingreso_exitoso'),
    path('adopcion-exitosa/', adopcion_exitosa, name='adopcion_exitosa'),
    path('adopcion-fallida/', adopcion_fallida, name='adopcion_fallida'),
    path('actualizar-borrar/', actualizar_borrar, name='actualizar_borrar'),
    path('detalle/<animal_id>/', detalle, name='detalle'),
    path('actualizar/<pk>/', actualizar.as_view(), name='actualizar'),
    path('borrar/<pk>/', borrar.as_view(), name='borrar')
    ]
    