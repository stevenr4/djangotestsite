# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-02 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_useraddress_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='address1',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='address2',
            new_name='address_2',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='lastname',
            new_name='last_name',
        ),
    ]