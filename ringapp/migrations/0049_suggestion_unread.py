# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-17 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ringapp', '0048_auto_20180210_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='unread',
            field=models.BooleanField(default=True),
        ),
    ]
