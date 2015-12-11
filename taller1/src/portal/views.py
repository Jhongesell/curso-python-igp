from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, request
from portal.forms import TicketForm
from portal.forms import VentaForm
from portal.helpers import HelperTicket
from django.http import HttpResponseRedirect
from portal.models import Ticket
from portal.models import Producto

from setuptools.command.bdist_egg import can_scan


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




def nuevaventa(request):
    form = VentaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            datos = form.cleaned_data
            num = form.cleaned_data['cantidad']
            if num % 2 == 1:
                nombre_producto_seleccionado = datos['producto'].nombre
                nuevo_nombre_producto = nombre_producto_seleccionado + ' ' + datos['cliente']
                producto = Producto()
                producto.nombre = nuevo_nombre_producto
                producto.precio = 1.23
                import random
                producto.cantidad = random.randint(10,20)
                producto.descripcion = 'Agregado desde Formulario Venta'
                producto.activo = True
                producto.save()


    return render(request,'venta/nueva.html', locals())




def ejemplosesiones(request):
    from django.core.urlresolvers import reverse

    contador = request.session.get('contador', 0)

    if (request.GET .get('reset', False)=='1'):
        # codigo para resetear
        # request.session['contador'] = 0
        del request.session['contador']
        return HttpResponseRedirect(reverse('rEjemploSesiones'))

    if (request.GET .get('incrementar', False)=='1'):
        # codigo para incrementar
        request.session['contador'] = contador + 1
        return HttpResponseRedirect(reverse('rEjemploSesiones'))



    return render(request,'ejemplo-sesiones.html', locals())












