# -*- coding: utf8 -*-

from django import forms
from django.db import models
from base.models import UserModel
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from base.datastructures import Enumeration
from prospectos.validators import validate_dni

# Create your models here.

class ProspectoManager(models.Manager):

    def varones(self):
        return self.filter(genero=Prospecto.OPCIONES_GENERO.MASCULINO)


class Prospecto(UserModel):

    OPCIONES_GENERO = Enumeration([
        (1, 'MASCULINO', _(u'Masculino')),
        (2, 'FEMENINO', _(u'Femenino'))
    ])

    dni = models.CharField(
        max_length=8,
        unique=True,
        validators=[validate_dni]
    )
    direccion = models.TextField(_(u'Dirección'))
    telefono = PhoneNumberField(_(u'Número telefónico'))
    genero = models.PositiveIntegerField(_(u'Género'),
        choices=OPCIONES_GENERO
    )

    objects = ProspectoManager()

    class Meta:
        verbose_name = _(u'Prospecto')
        verbose_name_plural = _(u'Prospectos')
