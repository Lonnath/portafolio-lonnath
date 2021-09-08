from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registro_proyecto, validar_usuario
def principal(request):
    return render(request, 'index.html')
def registro_proyectos(request):
    if request.method == 'POST':
        loginTmp = validar_usuario(request.POST)
        for fila in loginTmp.fields.values():
            print(fila)
        #if loginTmp.fields['usuario'] == 'lonnath' and loginTmp.fields['password'] == '1234':
        formulario = Registro_proyecto()
        return render(request, 'form_proyectos.html', {'formulario' : formulario})
    login = validar_usuario()
    return render(request, 'admin_proyectos.html', {'login' : login})