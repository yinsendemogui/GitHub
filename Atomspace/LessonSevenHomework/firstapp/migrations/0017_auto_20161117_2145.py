# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_auto_20161117_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.FileField(upload_to='profile_image'),
        ),
    ]
