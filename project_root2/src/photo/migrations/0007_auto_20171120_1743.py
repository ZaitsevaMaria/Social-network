# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('photo', '0006_auto_20171120_1539'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='tag',
            index_together=set([('object_id', 'content_type')]),
        ),
    ]