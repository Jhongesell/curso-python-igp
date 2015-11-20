# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Fecha y hora de creaci\xf3n')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Fecha y hora de modificaci\xf3n')),
                ('user', models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evaluador',
                'verbose_name_plural': 'Evaluadores',
            },
        ),
    ]
