# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170807_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(upload_to='images/stores/'),
        ),
    ]
