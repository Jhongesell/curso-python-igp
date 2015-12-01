# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Tiquete', 'verbose_name_plural': 'Tiquetes'},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='autor',
            field=models.ForeignKey(to='portal.Autor'),
        ),
    ]
