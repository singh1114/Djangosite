# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-05 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0012_auto_20160829_1848'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='cement',
            order_with_respect_to='Company_Name',
        ),
    ]
