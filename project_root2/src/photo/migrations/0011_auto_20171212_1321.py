# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 13:21
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_like_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_delete',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date_delete',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=150, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='like',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='like',
            name='date_delete',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='like',
            name='liked',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\x9b\xd0\xb0\xd0\xb9\xd0\xba'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='date_delete',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark_color',
            field=models.PositiveSmallIntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')], default=0, verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark_composition',
            field=models.PositiveSmallIntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')], default=0, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xbe\xd0\xb7\xd0\xb8\xd1\x86\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark_idea',
            field=models.PositiveSmallIntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')], default=0, verbose_name=b'\xd0\x98\xd0\xb4\xd0\xb5\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark_lighting',
            field=models.PositiveSmallIntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')], default=0, verbose_name=b'\xd0\x9e\xd1\x81\xd0\xb2\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='mark_settings',
            field=models.PositiveSmallIntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')], default=0, verbose_name=b'\xd0\x9d\xd0\xb0\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb9\xd0\xba\xd0\xb8/\xd1\x82\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0 \xd0\xb8\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Post', verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='photouser',
            name='about_user',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name=b'\xd0\x9e \xd1\x81\xd0\xb5\xd0\xb1\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='photouser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=b'avatars', verbose_name=b'\xd0\xb0\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='photouser',
            name='user_status',
            field=models.PositiveSmallIntegerField(choices=[(0, b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xb5\xd0\xbd'), (1, b'\xd0\x91\xd0\xb0\xd0\xbd (\xd1\x81\xd0\xbf\xd0\xb0\xd0\xbc)'), (2, b'\xd0\x91\xd0\xb0\xd0\xbd (\xd0\xbd\xd0\xb5\xd0\xb7\xd0\xb0\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f)'), (3, b'\xd0\x91\xd0\xb0\xd0\xbd (\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb6\xd0\xb0 \xd0\xb0\xd0\xba\xd0\xba\xd0\xb0\xd1\x83\xd0\xbd\xd1\x82\xd0\xb0)'), (4, b'\xd0\x91\xd0\xb0\xd0\xbd (\xd0\xbc\xd0\xbe\xd1\x88\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe)'), (5, b'\xd0\x91\xd0\xb0\xd0\xbd (\xd1\x80\xd0\xb5\xd0\xba\xd0\xbb\xd0\xb0\xd0\xbc\xd0\xb0)')], default=0),
        ),
        migrations.AlterField(
            model_name='photouser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_delete',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b'photo', verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(db_index=True, max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb5\xd0\xb3\xd0\xb0'),
        ),
    ]
