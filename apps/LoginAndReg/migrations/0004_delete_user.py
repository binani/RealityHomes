# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserDashboard', '0005_auto_20161117_2014'),
        ('LoginAndReg', '0003_auto_20161116_2300'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]