# -*- coding: utf8 -*-

from django.db import models
from automoviles.models import Automovil
from clientes.models import Cliente

# Create your models here.

class Venta(models.Model):
    automovil = models.ForeignKey(Automovil)
    comprador = models.ForeignKey(Cliente,
        related_name='ventas_como_comprador'
    )
    vendedor = models.ForeignKey(Cliente,
        related_name='ventas_como_vendedor'
    )
    observaciones = models.TextField(blank=True, null=True)
    fecha_venta = models.DateField()

    class Meta:
        verbose_name = u'Venta'
        verbose_name_plural = u'Ventas'

    def __unicode__(self):
        return u"Venta Nro. %d" % self.pk
