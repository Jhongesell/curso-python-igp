from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, request
from portal.forms import TicketForm
from portal.helpers import HelperTicket
from django.http import HttpResponseRedirect
from portal.models import Ticket


def saluda(request):
    return HttpResponse('[Portal] Hola IGP +')


def saludahtml(request):
    return render(request, 'hola.html')

def conlayout(request):
    return render(request, 'conlayout.html')

def listartickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket/listar.html', locals())

def nuevoticket(request):
    form = TicketForm
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ticket/listar/')
    return render(request, 'ticket/nuevo.html', locals())

def cerrarticket(request, id):
    if request.method == 'POST':
        ticket = Ticket.objects.get(id=id)
        ticket.estado = 'cerrado'
        ticket.save()
        return HttpResponseRedirect('/ticket/listar/')
    return render(request, 'ticket/cerrar.html', locals())


def editarticket(request, id):
    ticket = Ticket.objects.get(id=id)
    form = TicketForm(request.POST or None, instance=ticket)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ticket/listar/')
    return render(request, 'ticket/editar.html', locals())
