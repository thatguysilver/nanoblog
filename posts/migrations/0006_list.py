# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20170623_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True, verbose_name='date published')),
            ],
        ),
    ]