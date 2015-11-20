# -*- coding: utf8 -*-

from unidecode import unidecode

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django_extensions.db.fields import CreationDateTimeField
from django_extensions.db.fields import ModificationDateTimeField

# Create your models here.

class BaseModel(models.Model):

    created = CreationDateTimeField(
        _(u'Fecha y hora de creación')
    )
    modified = ModificationDateTimeField(
        _(u'Fecha y hora de modificación')
    )

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True

    def __str__(self):
        return unidecode(self.__unicode__())

    def __unicode__(self):
        return u'Objeto %s (PK: %d)' % (
            self.__class__.name,
            self.pk
        )

    def __repr__(self):
        return '<%s object %s (PK: %d) at %s>' % (
            self.__class__.name,
            str(self),
            self.pk,
            hex(id(self))
        )


class UserModel(BaseModel):

    user = models.ForeignKey(User,
        verbose_name=_(u'Usuario')
    )

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True

    def __unicode__(self):
        return self.obtener_nombre_completo()

    def obtener_nombres(self):
        if self.user:
            return self.user.first_name
        else:
            return u''

    def asignar_nombres(self, nombres):
        if self.user:
            self.user.first_name = nombres

    def obtener_apellidos(self):
        if self.user:
            return self.user.last_name
        else:
            return u''

    def asignar_apellidos(self, apellidos):
        if self.user:
            self.user.last_name = apellidos

    def obtener_correo(self):
        if self.user:
            return self.user.email
        else:
            return ''

    def asignar_correo(self, correo):
        if self.user:
            self.user.email = correo

    def obtener_nombre_completo(self):
        return ('%s %s'% (
            self.obtener_nombres(),
            self.obtener_apellidos()
        )).strip()

    nombres = property(obtener_nombres, asignar_nombres)
    apellidos = property(obtener_apellidos, asignar_apellidos)
    correo = property(obtener_correo, asignar_correo)
