# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20161117_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='avatar_image',
            field=models.CharField(default='E:\\Atomspace\\LessonSevenHomework\\firstapp/static/images/', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='cover_image'),
        ),
    ]