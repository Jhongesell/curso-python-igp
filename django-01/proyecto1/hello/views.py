# -*- coding: utf8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def saludar(request):
    params = {}
    params['content_type'] = 'text/plain'
    return HttpResponse('¡Hola mundo!', **params)

def saludar_con_nombre(request, nombre):
    saludo = u'¡Hola %s!' % nombre
    return HttpResponse(saludo, content_type='text/plain')

def saludar2(request):
    nombre = request.GET.get('nombre', None)
    if nombre:
        saludo =  u'¡Hola %s!' % nombre
    else:
        saludo = u'¡Hola mundo!'
    return HttpResponse(saludo, content_type='text/plain')

def saludar3(request):
    nombre = request.GET.get('nombre', None)
    contexto = {}
    contexto['nombre'] = nombre
    return render(request, 'hello/saludar.html', context=contexto)

def bs(request):
    context = {}
    return render(request, 'hello/vistabs.html', context)

def otrabs(request):
    context = {}
    return render(request, 'hello/otrabs.html', context)









