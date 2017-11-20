# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0009_bookinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d65c15b6-b67f-411d-a68f-64a2382269cd'), help_text='Unique Id For the Particular book across whole library', primary_key=True, serialize=False, unique=True),
        ),
    ]
