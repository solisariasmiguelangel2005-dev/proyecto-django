from django import forms
from .models import Alumnos, Comentario, ComentarioContacto
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class CustomFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ['titulo', 'descripcion', 'archivo']
        widgets = {
            'archivo': CustomFileInput
        }