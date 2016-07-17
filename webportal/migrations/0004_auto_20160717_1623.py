# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0003_auto_20160717_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cement',
            name='grade',
        ),
        migrations.AddField(
            model_name='cement',
            name='grade_of_cement',
            field=models.CharField(choices=[('33', '33'), ('43', '43'), ('53', '53')], default='33', max_length=9),
        ),
    ]
