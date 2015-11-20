from django.contrib import admin

# Register your models here.

from automoviles.models import Automovil

# Register your models here.

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('id', 'placa', 'fecha_fabricacion')

admin.site.register(Automovil, AutomovilAdmin)
