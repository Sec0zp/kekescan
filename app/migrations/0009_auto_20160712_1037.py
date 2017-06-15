# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 02:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160712_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burp',
            name='host',
            field=models.CharField(max_length=200, verbose_name=b'HOST'),
        ),
        migrations.AlterField(
            model_name='burp',
            name='queryed',
            field=models.IntegerField(default=0, max_length=1, verbose_name=b'queryed'),
        ),
        migrations.AlterField(
            model_name='icpcheck',
            name='insert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 10, 37, 19, 460420), null=True),
        ),
        migrations.AlterField(
            model_name='subdomainbrute',
            name='fuzz_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 10, 37, 19, 460995), null=True),
        ),
    ]