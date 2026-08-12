from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name='eliminarComentario'),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('consultas/', views_registros.consultas, name='consultas'),
    path('consultas1/', views_registros.consultar1, name='Consultas1'),
    path('consultas2/', views_registros.consultar2, name='Consultas2'),
    path('consultas3/', views_registros.consultar3, name='Consultas3'),
    path('consultas4/', views_registros.consultar4, name='Consultas4'),
    path('consultas5/', views_registros.consultar5, name='Consultas5'),
    path('consultas6/', views_registros.consultar6, name='Consultas6'),
    path('consultas7/', views_registros.consultar7, name='Consultas7'),
    path('consultas8/', views_registros.consultar8, name='Consultas8'),
    path('consultasSQL/', views_registros.consultasSQL, name='sql'),

    path('comentariosPorFecha/', views_registros.comentariosPorFecha, name='comentariosFecha'),
    path('comentariosPorExpresion/', views_registros.comentariosPorExpresion, name='comentariosExpresion'),
    path('comentariosPorUsuario/', views_registros.comentariosPorUsuario, name='comentariosUsuario'),
    path('comentariosStartswith/', views_registros.comentariosStartswith, name='comentariosStartswith'),
    path('comentariosEndswith/', views_registros.comentariosEndswith, name='comentariosEndswith'),

    path('comentariosPorFechaSQL/', views_registros.comentariosPorFechaSQL, name='comentariosFechaSQL'),
    path('comentariosPorExpresionSQL/', views_registros.comentariosPorExpresionSQL, name='comentariosExpresionSQL'),
    path('comentariosPorUsuarioSQL/', views_registros.comentariosPorUsuarioSQL, name='comentariosUsuarioSQL'),
    path('comentariosStartswithSQL/', views_registros.comentariosStartswithSQL, name='comentariosStartswithSQL'),
    path('comentariosEndswithSQL/', views_registros.comentariosEndswithSQL, name='comentariosEndswithSQL'),
    path('subir', views_registros.archivos, name='subir'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)