# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-16 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20181016_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='create_date',
            field=models.CharField(default='2018-10-16 21:44:09', max_length=40, verbose_name='创建时间'),
        ),
    ]
