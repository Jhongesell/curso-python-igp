# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_ejemplo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('cantidad', models.SmallIntegerField()),
                ('descripcion', models.TextField(max_length=3000)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]
