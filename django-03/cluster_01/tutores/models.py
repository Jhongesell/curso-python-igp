from django.db import models
from base.models import BaseModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Tutor(BaseModel):

    nombres = models.CharField(
        verbose_name=_(u'Nombres'),
        max_length=64
    )

    apellidos = models.CharField(
        verbose_name=_(u'Apellidos'),
        max_length=64
    )

    class Meta:
        verbose_name = _(u'Tutor')
        verbose_name_plural = _(u'Tutores')

    def __unicode__(self):
        return self.obtener_nombre_completo()

    def __repr__(self):
        return '<Tutor object %s (PK: %d) at %s>' % (
            str(self),
            self.pk,
            hex(id(self))
        )

    def obtener_nombre_completo(self):
        return ('%s %s'% (
            self.nombres,
            self.apellidos
        )).strip()
