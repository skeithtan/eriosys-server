# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-01 04:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0037_auto_20171201_0442'),
        ('institutions', '0036_requirement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studyfield',
            name='program',
        ),
        migrations.DeleteModel(
            name='StudyField',
        ),
    ]
