# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20171212_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 22, 55, 18, 324591)),
        ),
    ]
