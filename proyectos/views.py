from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto, Experiencias_cv, Estudios_cv, Descripcion_cv
import os
def principal(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos' : proyectos})
def informacion(request):
    informacion = Descripcion_cv.objects.all()
    return render(request, 'informacion.html', {'informaciones' : informacion})
def experiencias(request):
    experiencias = Experiencias_cv.objects.all()
    return render(request, 'experiencias.html', {'experiencias' : experiencias})
def estudios(request):
    estudios = Estudios_cv.objects.all()
    return render(request, 'estudios.html', {'estudios' : estudios})
