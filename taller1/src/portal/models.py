from django.db import models

# Create your models here.
TICKET_ESTADOS = (
    ('nuevo', 'Nuevo'),
    ('asignado', 'Asignado'),
    ('en-progreso', 'En Progreso'),
    ('completado', 'Completado'),
    ('cerrado', 'Cerrado'),
)


class Ticket(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(max_length=2000)
    estado = models.CharField(max_length=32, choices=TICKET_ESTADOS)
    autor = models.CharField(max_length=120, blank=True)

    def __unicode__(self):
        return '[%s] %s (%s)' % (self.estado, self.titulo, self.autor)



