# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20161110_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aritcle',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
