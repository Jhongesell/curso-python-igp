from django.db import models

# Create your models here.
from setuptools.command.develop import develop

TICKET_ESTADOS = (
    ('nuevo', 'Nuevo'),
    ('asignado', 'Asignado'),
    ('en-progreso', 'En Progreso'),
    ('completado', 'Completado'),
    ('cerrado', 'Cerrado'),
)

class Autor(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email


class Ticket(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(max_length=2000)
    estado = models.CharField(max_length=32, choices=TICKET_ESTADOS)
    # autor = models.CharField(max_length=120, blank=True)
    autor = models.ForeignKey(Autor, blank=True)

    class Meta:
        verbose_name = u'Tiquete'
        verbose_name_plural = u'Tiquetes'

    def __unicode__(self):
        return '[%s] %s (%s)' % (self.estado, self.titulo, self.titulo)



class Ejemplo(models.Model):
    campo = models.TextField(max_length=2000)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.SmallIntegerField()
    descripcion = models.TextField(max_length=3000)
    activo = models.BooleanField()
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = u'Producto'
        verbose_name_plural = u'Productos'







