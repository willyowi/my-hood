# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-15 17:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 17, 8, 33, 438482, tzinfo=utc)),
        ),
    ]
