from django.urls import path
from inicio.views import inicio,ingresar,adoptar

urlpatterns=[
    path('', inicio, name='inicio'),
    path('ingresar/', ingresar, name='ingresar'),
    path('adoptar/', adoptar, name='adoptar')
    ]
    