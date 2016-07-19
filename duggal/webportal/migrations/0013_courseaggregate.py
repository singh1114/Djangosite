# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0012_auto_20160718_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAggregate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Place', models.CharField(max_length=15, verbose_name='Place of Import', choices=[('Anandpur_Sahib', 'Anandpur Sahib'), ('Pathankot', 'Pathankot')])),
                ('Size', models.CharField(max_length=5, verbose_name='Size of course', choices=[('10', '10 mm'), ('20', '20 mm'), ('30', '30 mm')])),
                ('Amount', models.CharField(max_length=15, verbose_name='Choose a unit', choices=[('100', '100 foot cube'), ('250', '250 foot cube'), ('1000', '1000 foot cube')])),
            ],
        ),
    ]
