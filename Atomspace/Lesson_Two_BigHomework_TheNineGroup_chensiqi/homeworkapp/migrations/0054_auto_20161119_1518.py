# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkapp', '0053_auto_20161119_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('normal', 'normal'), ('like', 'like'), ('dislike', 'dislike')], max_length=10),
        ),
    ]
