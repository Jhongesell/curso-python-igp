from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User)
    dni = models.CharField(max_length=8, unique=True)

    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'

    def __unicode__(self):
        if self.usuario is not None:
            return self.usuario.get_full_name()
        else:
            return u'Cliente'
