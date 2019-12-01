# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-01 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('bug_title', models.CharField(max_length=256)),
                ('bug_description', models.TextField()),
            ],
        ),
    ]