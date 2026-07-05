from django.shortcuts import render, redirect
from registros.forms import ComentarioContactoForm
from registros.models import ComentarioContacto  

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