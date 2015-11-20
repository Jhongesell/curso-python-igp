# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
        migrations.AddField(
            model_name='venta',
            name='comprador',
            field=models.ForeignKey(related_name='ventas_como_comprador', default=1, to='clientes.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='vendedor',
            field=models.ForeignKey(related_name='ventas_como_vendedor', default=1, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]
