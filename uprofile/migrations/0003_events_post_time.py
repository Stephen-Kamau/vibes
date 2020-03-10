# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-03 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uprofile', '0002_auto_20200302_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='post_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
