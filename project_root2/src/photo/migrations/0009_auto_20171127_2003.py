# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('photo', '0008_auto_20171121_1657'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='comment',
            index_together=set([('object_id', 'content_type')]),
        ),
    ]
