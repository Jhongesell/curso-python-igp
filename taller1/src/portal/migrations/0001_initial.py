# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=120)),
                ('descripcion', models.TextField(max_length=2000)),
                ('estado', models.CharField(max_length=32, choices=[(b'nuevo', b'Nuevo'), (b'asignado', b'Asignado'), (b'en-progreso', b'En Progreso'), (b'completado', b'Completado'), (b'cerrado', b'Cerrado')])),
            ],
        ),
    ]
