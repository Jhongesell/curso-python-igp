# -*- coding: utf8 -*-
from django.db import models

# Create your models here.

class Automovil(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    fecha_fabricacion = models.DateField()

    class Meta:
        verbose_name = u'Automovil'
        verbose_name_plural = u'Automóviles'

    def __unicode__(self):
        return self.placa
