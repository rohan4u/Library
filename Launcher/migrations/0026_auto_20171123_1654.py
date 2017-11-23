# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0025_auto_20171123_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='LendingDate',
        ),
        migrations.RemoveField(
            model_name='books',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='books',
            name='Publisher_Name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='Year',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='page_amount',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]