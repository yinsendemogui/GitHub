# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20161117_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='/static/cover_image/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.FileField(upload_to='/static/profile_image/'),
        ),
    ]
