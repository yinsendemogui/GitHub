# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkapp', '0086_auto_20161119_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')], max_length=10),
        ),
    ]
