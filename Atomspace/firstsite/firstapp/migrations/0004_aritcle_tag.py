# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20161110_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='aritcle',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]