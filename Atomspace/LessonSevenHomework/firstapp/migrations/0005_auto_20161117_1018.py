# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20161117_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='avatar_image',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='createtime',
            field=models.DateField(auto_now=True),
        ),
    ]
