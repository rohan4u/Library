# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0023_auto_20171123_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
