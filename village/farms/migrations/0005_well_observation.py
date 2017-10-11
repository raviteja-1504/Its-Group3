# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0004_well_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='well_observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth_in_meters', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_of_observation', models.DateField(null=True)),
                ('wateryield', models.DecimalField(decimal_places=2, max_digits=8)),
                ('well_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.well_info')),
            ],
        ),
    ]