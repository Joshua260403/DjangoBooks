# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 05:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170922_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='publication_date',
        ),
    ]
