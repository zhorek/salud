from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def inicio(request):
    return render(request,'home/inicio.html')

def nosotros(request):
    return render(request,'home/nosotros.html')

def campañas(request):
    return render(request,'home/campañas.html')

def contacto(request):
    return render(request,'home/contacto.html')

def prueba(request):
    return render(request,'home/prueba.html')

