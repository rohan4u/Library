# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0021_auto_20171123_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='subj_code',
        ),
        migrations.AddField(
            model_name='books',
            name='subj_code',
            field=models.ForeignKey(default=None, help_text='Select Subject of the book', on_delete=django.db.models.deletion.CASCADE, to='Launcher.Subject'),
        ),
    ]