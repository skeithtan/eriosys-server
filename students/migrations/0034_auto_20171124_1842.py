# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-24 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0033_auto_20171124_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outboundstudentprogram',
            name='application_requirement',
            field=models.ManyToManyField(null=True, to='institutions.Requirement'),
        ),
    ]