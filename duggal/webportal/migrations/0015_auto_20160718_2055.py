# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0014_courseaggregate_price_of_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseaggregate',
            old_name='Amount',
            new_name='Amount_of_course',
        ),
        migrations.RenameField(
            model_name='courseaggregate',
            old_name='Place',
            new_name='Place_of_course',
        ),
        migrations.RenameField(
            model_name='courseaggregate',
            old_name='Size',
            new_name='Size_of_course',
        ),
    ]
