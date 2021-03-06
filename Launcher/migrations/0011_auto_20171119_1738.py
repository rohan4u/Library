# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0010_auto_20171119_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique Id For the Particular book across whole library', primary_key=True, serialize=False, unique=True),
        ),
    ]
