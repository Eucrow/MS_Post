# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_categoria', models.CharField(choices=[('POL', 'Política'), ('ECO', 'Economía'), ('SOC', 'Sociedad'), ('DEP', 'Deporte'), ('CUL', 'Cultura'), ('CIE', 'Ciencia')], default='CUL', max_length=3)),
            ],
        ),
    ]
