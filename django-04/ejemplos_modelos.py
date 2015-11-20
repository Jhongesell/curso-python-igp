from django.db import models

class Automovil(models.Model):
    pass

class Persona(models.Model):
    dni = models.CharField(
        max_length=8,
        unique=True
    )


class Venta(models.Models):
    automovil = models.ForeignKey(Automovil)
    comprador = models.ForeignKey(Persona,
        related_name='ventas_como_comprador'
    )
    vendedor = models.ForeignKey(Persona,
        related_name='ventas_como_vendedor'
    )

###

auto1 = Automovil.objects.get(pk=1)
auto1.objects.ventas.all()

##

class Empleado(models.Model):
    codigo = models.CharField(max_length=12, unique=True)
    jefe = models.ForeignKey('Empleado')


Persona.objects.ventas_como_comprador.all()
