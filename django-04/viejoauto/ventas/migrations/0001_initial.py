# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automoviles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('fecha_venta', models.DateField()),
                ('automovil', models.ForeignKey(to='automoviles.Automovil')),
            ],
            options={
                'verbose_name': 'Automovil',
                'verbose_name_plural': 'Autom\xf3viles',
            },
        ),
    ]
