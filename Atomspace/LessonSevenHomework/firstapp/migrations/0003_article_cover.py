# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20161105_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.FileField(null=True, upload_to='cover_image'),
        ),
    ]
