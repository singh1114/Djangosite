# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0009_auto_20160815_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
