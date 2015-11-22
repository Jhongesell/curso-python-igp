from django.contrib import admin
from cluster_01.admin import admin_site

# Register your models here.

from prospectos.models import Prospecto
from prospectos.forms import ProspectoForm

class ProspectoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombres', 'apellidos', 'dni', 'telefono','created'
    )
    form = ProspectoForm

admin_site.register(Prospecto, ProspectoAdmin)
