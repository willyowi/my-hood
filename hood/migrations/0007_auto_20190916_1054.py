# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-16 07:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_auto_20190916_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 16, 7, 54, 59, 368622, tzinfo=utc)),
        ),
    ]
