# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0002_auto_20171111_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
