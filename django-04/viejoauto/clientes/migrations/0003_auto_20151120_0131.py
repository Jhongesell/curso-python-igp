# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20151120_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
