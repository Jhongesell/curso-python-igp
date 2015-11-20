# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(unique=True, max_length=7)),
                ('fecha_fabricacion', models.DateField()),
            ],
            options={
                'verbose_name': 'Automovil',
                'verbose_name_plural': 'Autom\xf3viles',
            },
        ),
    ]
