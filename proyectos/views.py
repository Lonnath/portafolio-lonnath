from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registro_proyecto, validar_usuario
def principal(request):
    return render(request, 'index.html')
def registro_proyectos(request):
    if request.method == 'POST':
        loginTmp = validar_usuario(request.POST)
        if loginTmp.is_valid():
            informacion = loginTmp.cleaned_data
            if informacion['usuario'] == 'lonnath' and informacion['password'] == 'Vagato1697':
                formulario = Registro_proyecto()
                return render(request, 'form_proyectos.html', {'formulario' : formulario})
            acces = 'Usuario o Contraseña Incorrectos'
            acc_sty = 'badge bg-danger'
    else:
        acces = ''
        acc_sty = ''
    login = validar_usuario()
    
    return render(request, 'admin_proyectos.html', {'login' : login, 'acceso' : acces, 'acceso_estilo' : acc_sty})