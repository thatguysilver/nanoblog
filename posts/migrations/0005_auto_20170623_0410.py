# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170623_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='date published'),
        ),
    ]
