# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0007_auto_20170913_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm_info',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='farm_info',
            name='lon',
        ),
    ]
