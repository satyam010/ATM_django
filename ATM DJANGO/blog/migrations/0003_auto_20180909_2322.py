# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-09 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180909_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logininfo',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
