# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 06:43
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(default=' ', max_length=128, verbose_name='标题')),
                ('blog_content', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('blog_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Release_posts', to=settings.AUTH_USER_MODEL, verbose_name='发布者')),
            ],
            options={
                'verbose_name': '博文信息',
                'verbose_name_plural': '博文信息',
            },
        ),
    ]
