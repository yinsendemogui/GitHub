# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkapp', '0075_auto_20161119_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10),
        ),
    ]
