# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20171115_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencyaddresshistory',
            name='user',
            field=models.CharField(blank=True, default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.CharField(blank=True, default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentprogram',
            name='user',
            field=models.CharField(blank=True, default='', max_length=32),
            preserve_default=False,
        ),
    ]