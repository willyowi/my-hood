# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-16 07:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_auto_20190916_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='NO IMAGE', upload_to='hoodpics/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 16, 7, 45, 13, 385007, tzinfo=utc)),
        ),
    ]