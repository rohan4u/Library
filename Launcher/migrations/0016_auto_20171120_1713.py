# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0015_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roll_number',
            field=models.IntegerField(),
        ),
    ]