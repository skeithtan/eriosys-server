# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0010_auto_20171104_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='contact_person_email',
            field=models.CharField(blank=True, default='', max_length=256),
            preserve_default=False,
        ),
    ]
