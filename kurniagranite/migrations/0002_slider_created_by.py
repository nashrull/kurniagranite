# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-31 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurniagranite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='created_by',
            field=models.CharField(default='Session Login', max_length=32),
            preserve_default=False,
        ),
    ]
