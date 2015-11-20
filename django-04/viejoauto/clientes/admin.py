from django.contrib import admin
from clientes.models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )

    def nombre(self, instance):
        return instance.usuario.get_full_name()

admin.site.register(Cliente, ClienteAdmin)
