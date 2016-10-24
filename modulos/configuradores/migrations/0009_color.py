# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-18 00:13
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuradores', '0008_auto_20161017_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, editable=False)),
                ('codigo', models.CharField(blank=True, max_length=255, unique=True)),
                ('color', colorfield.fields.ColorField(default='#0000000', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Colores',
            },
        ),
    ]
