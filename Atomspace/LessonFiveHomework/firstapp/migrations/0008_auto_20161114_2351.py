# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20161114_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.CharField(default='E:\\Atomspace\\LessonFiveHomework\\firstapp/static/images/default.png', max_length=100),
        ),
    ]
