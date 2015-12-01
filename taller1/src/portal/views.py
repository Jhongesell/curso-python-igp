from django.shortcuts import render
from django.http import HttpResponse, request
from portal.forms import TicketForm


def saluda(request):
    return HttpResponse('[Portal] Hola IGP +')


def saludahtml(request):
    return render(request, 'hola.html')


def conlayout(request):
    return render(request, 'conlayout.html')

def nuevoticket(request):
    form = TicketForm
    return render(request, 'ticket/nuevo.html', {'formigp': form})