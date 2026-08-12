from datetime import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

from django.shortcuts import render, redirect
from httpx import request
from registros.forms import ComentarioContactoForm
from registros.models import ComentarioContacto  
from django.shortcuts import get_object_or_404
from django.db.models import Q
from registros.models import Alumnos

def registros(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registros')
    else:
        form = ComentarioContactoForm()

    return render(request, "registros/contacto.html", {'form': form})

def contacto(request):
    return render(request, "registros/contacto.html")

def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})

def eliminarComentarioContacto(request, id):
    confirmacion = 'registros/confirmarEliminacion.html'
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})
    return render(request, confirmacion, {'comentario': comentario})


def consultarComentarioIndividual(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    return render(request, "registros/editarComentario.html", 
        {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/consultarComentario.html',
                {'comentarios': comentarios})
    return render(request, 'registros/editarComentario.html', 
        {'comentario': comentario})


def consultas(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'registros/consultas.html', {
        'alumnos': alumnos,
    })

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

#NUEVAS DOS CONSULTAS


def consultar4(request): #ALUMNOS QUE NO SON DE LA CARRERA DE TI
    alumnos = Alumnos.objects.exclude(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar5(request): #ALUMNOS QUE SU MATRICULA TERMINA EN TI
    alumnos = Alumnos.objects.filter(matricula__endswith="TI")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar6(request): #
    alumnos = Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    fechaInicio = datetime(2026, 8, 1)
    fechaFin = datetime(2026, 8, 31)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar8(request): #
    alumnos = Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera = "TI" ORDER BY turno DESC')
    return render(request, 'registros/consultas.html', {
        'alumnos': alumnos,
    })


#CONSULTAS ORM

def comentariosPorFecha(request):
    fechaInicio = datetime(2026, 6, 20)
    fechaFin = datetime(2026, 8, 4)
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})


def comentariosPorExpresion(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="hola")
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})


def comentariosPorUsuario(request):
    comentarios = ComentarioContacto.objects.filter(usuario="Angel Miguel")
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})


def comentariosStartswith(request):
    comentarios = ComentarioContacto.objects.filter(usuario__istartswith="M")
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})

def comentariosEndswith(request):
    comentarios = ComentarioContacto.objects.filter(usuario__iendswith="l")
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})



#CONSULTAS SQL

def comentariosPorFechaSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE created BETWEEN "2026-06-20" AND "2026-08-04"')
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})


def comentariosPorExpresionSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE mensaje LIKE "%hola%"')
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})


def comentariosPorUsuarioSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE usuario = "Angel Miguel"')
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})


def comentariosStartswithSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE usuario LIKE "M%"')
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})

def comentariosEndswithSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE usuario LIKE "%l"')
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'registros/archivos.html')
        else:
            messages.error(request, 'Error al procesar el formulario.')
            return render(request, 'registros/archivos.html')  # 👈 agregado
    else:
        return render(request, 'registros/archivos.html', {'archivo': Archivos})