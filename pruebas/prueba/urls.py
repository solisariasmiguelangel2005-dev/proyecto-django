from django.contrib import admin
from django.urls import path

from prueba.inicio import views as views_inicio
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name='principal'),
    path('contacto/', views_registros.registros, name='contacto'),
    path('formulario/', views_inicio.formulario, name='formulario'),
    path('nombre/', views_inicio.nombre, name='nombre'),
    path('ejemplo/', views_inicio.ejemplo, name='ejemplo'),
    path('registros/', views_registros.registros, name='registros'),
    path('consultarComentario/', views_registros.consultarComentario, name='consultarComentario'),
]