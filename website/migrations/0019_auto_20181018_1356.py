# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-18 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20181017_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='create_date',
            field=models.CharField(default='2018-10-18 13:56:50', max_length=40, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='new',
            name='create_date',
            field=models.CharField(default='2018-10-18 13:56:50', max_length=40, verbose_name='创建时间'),
        ),
    ]