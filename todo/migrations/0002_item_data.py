# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='data',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
