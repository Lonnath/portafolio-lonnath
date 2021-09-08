from django import forms
from django.forms import widgets
from .models import Proyectos
class validar_usuario(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
        
class Registro_proyecto(forms.Form):
    error_css_class = 'alert alert-danger'
    required_css_class = 'alert alert-secondary'
    nombre_proyecto = forms.CharField(label='Nombre del Proyecto')
    url_proyecto = forms.URLField(label='Url del Proyecto')
    descripcion = forms.CharField(label='Descripción')
    class Meta:
        model = Proyectos
        
    