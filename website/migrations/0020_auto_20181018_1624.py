# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-18 08:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20181018_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='uuid')),
                ('file_path', models.CharField(default='', max_length=150, verbose_name='文件保存路径')),
                ('is_top', models.BooleanField(default=False, verbose_name='是否置顶')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否已删除(文件并未删除只是做标记)')),
                ('upload_date', models.CharField(default='2018-10-18 16:24:30', max_length=40, verbose_name='创建时间')),
                ('upload_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='create_date',
            field=models.CharField(default='2018-10-18 16:24:30', max_length=40, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='new',
            name='create_date',
            field=models.CharField(default='2018-10-18 16:24:30', max_length=40, verbose_name='创建时间'),
        ),
    ]