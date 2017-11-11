# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2_rel', to='sudoku.GameUser'),
        ),
    ]
