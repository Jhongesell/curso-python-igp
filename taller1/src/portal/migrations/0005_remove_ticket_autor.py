# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20151201_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='autor',
        ),
    ]
