from django.contrib import admin
from portal.models import Ticket
from portal.models import Autor
from portal.models import Ejemplo
from portal.models import Producto

admin.site.register(Ticket)
admin.site.register(Autor)
admin.site.register(Ejemplo)
admin.site.register(Producto)

