from django.contrib import admin
from cluster_01.admin import admin_site

# Register your models here.

from prospectos.models import Prospecto

class ProspectoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombres', 'apellidos', 'dni', 'telefono','created'
    )

admin_site.register(Prospecto, ProspectoAdmin)
