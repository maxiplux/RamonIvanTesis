# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuradores', '0004_tipomateriaprima'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoBodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Bodega',
            },
        ),
    ]
