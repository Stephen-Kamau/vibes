# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-03 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0004_auto_20200301_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='followers',
            name='is_following',
            field=models.BooleanField(default=False),
        ),
    ]
