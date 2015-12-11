# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_ticket_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejemplo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campo', models.TextField(max_length=2000)),
            ],
        ),
    ]
