# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170824_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
