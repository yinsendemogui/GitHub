# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 02:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_article_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='img',
            new_name='avatar_image',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='cover',
            new_name='cover_image',
        ),
    ]
