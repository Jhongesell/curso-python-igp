from django.shortcuts import render
from .forms import ProspectoForm
from .forms import DemoForm

def nuevo(request):

    form = ProspectoForm()

    return render(request, 'prospectos/nuevo.html', {
        'form': form,
        'msg': 'Ten cui<b>da</b>do...',
    })


def demoform(request):
    formulario = DemoForm()

    return render(request, 'prospectos/demoform.html', {
        'username': 'juan',
        'formulario': formulario,
        'advertencia': 'Por favor, ten cuidado con...',
        'msg': 'Tienes un nuevo mensaje sin leer',
    })
