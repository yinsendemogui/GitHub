# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
