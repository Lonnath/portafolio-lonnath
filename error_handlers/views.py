from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import request
def error_400(request, exception):
    return HttpResponse('Error 400 todo bien')
def error_403(request, exception):
    return HttpResponse('Error 403 todo bien')
def error_404(request, exception):
    return render(request, 'error_404.html')
def error_500(request):
    return render(request, 'error_500.html')