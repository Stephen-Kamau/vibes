# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-22 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell_goods',
            name='GLocation',
            field=models.CharField(default='Narobi/Kenya', max_length=255),
        ),
    ]
