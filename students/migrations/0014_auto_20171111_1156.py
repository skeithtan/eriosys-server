# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-11 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20171109_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprogram',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.StudyField'),
        ),
    ]