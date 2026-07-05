from django import forms
from .models import Alumnos, Comentario, ComentarioContacto

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje'] 