# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 09:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_auto_20160125_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='transaction_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]