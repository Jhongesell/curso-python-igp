from django.shortcuts import render
from django.http import HttpResponse, request


def saluda(request):
    return HttpResponse('[Portal] Hola IGP +')


def saludahtml(request):
    return render(request, 'hola.html')


def conlayout(request):
    return render(request, 'conlayout.html')