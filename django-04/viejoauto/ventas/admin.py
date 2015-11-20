from django.contrib import admin
from ventas.models import Venta

# Register your models here.

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'automovil', 'comprador', 'vendedor','fecha_venta')

admin.site.register(Venta, VentaAdmin)
