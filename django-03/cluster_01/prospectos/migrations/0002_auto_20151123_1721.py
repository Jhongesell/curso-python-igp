# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import prospectos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('prospectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospecto',
            name='dni',
            field=models.CharField(unique=True, max_length=8, validators=[prospectos.validators.validate_dni]),
        ),
    ]
