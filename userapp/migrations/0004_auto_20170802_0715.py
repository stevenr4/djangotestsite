# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-02 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_auto_20170802_0425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'verbose_name_plural': 'user addresses'},
        ),
    ]
