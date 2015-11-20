# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import phonenumber_field.modelfields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Fecha y hora de creaci\xf3n')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Fecha y hora de modificaci\xf3n')),
                ('dni', models.CharField(unique=True, max_length=8)),
                ('direccion', models.TextField(verbose_name='Direcci\xf3n')),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='N\xfamero telef\xf3nico')),
                ('genero', models.PositiveIntegerField(verbose_name='G\xe9nero', choices=[(1, 'Masculino'), (2, 'Femenino')])),
                ('user', models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Prospecto',
                'verbose_name_plural': 'Prospectos',
            },
        ),
    ]
