# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-24 01:56
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('titulo', models.CharField(blank=True, max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='titulo', unique=True)),
                ('resumen', models.TextField(blank=True, null=True)),
                ('contenido', models.TextField()),
            ],
            options={
                'ordering': ['titulo'],
                'abstract': False,
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, editable=False)),
                ('sub_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enciclopedia.Categoria')),
            ],
            options={
                'ordering': ['nombre'],
                'abstract': False,
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('archivo', models.ImageField(upload_to='articulos/imagenes/')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enciclopedia.Articulo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Portada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, unique=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, editable=False)),
                ('archivo', models.ImageField(upload_to='portada')),
            ],
            options={
                'ordering': ['nombre'],
                'abstract': False,
                'verbose_name': 'Portada',
                'verbose_name_plural': 'Portadas',
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enciclopedia.Categoria'),
        ),
    ]
