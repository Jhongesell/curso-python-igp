# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_remove_ticket_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='autor',
            field=models.ForeignKey(default=1, blank=True, to='portal.Autor'),
            preserve_default=False,
        ),
    ]
