# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Launcher', '0007_auto_20171115_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Subject Name (e.g Film, Studio, Television)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='subj_code',
            field=models.ManyToManyField(help_text='Select Subject of the book', to='Launcher.Subject'),
        ),
    ]
