# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20161126_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('normal', 'normal'), ('like', 'like'), ('dislike', 'dislike')], max_length=10),
        ),
    ]
