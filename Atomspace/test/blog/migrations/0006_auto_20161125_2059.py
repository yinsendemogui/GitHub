# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161125_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('normal', 'normal'), ('like', 'like')], max_length=10),
        ),
    ]
