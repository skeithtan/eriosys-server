# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0006_auto_20171103_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorandumlinkage',
            name='linkage',
            field=models.CharField(choices=[('S', 'Scholarship'), ('OI', 'OJT/Internship'), ('FE', 'Faculty Exchange'), ('SE', 'Student Exchange'), ('RE', 'Researcher / Expert Exchange'), ('SP', 'Support for Projects Exchange'), ('RP', 'Research and Publication'), ('AP', 'Academic Program'), ('PF', 'Project Funding'), ('EMPI', 'Exchange of Materials, Publications and Information'), ('CE', 'Cultural Exchange'), ('SAMC', 'Seminars and Academic Meetings / Conferences'), ('TAP', 'Technical or Administrative Programs'), ('O', 'Established Office'), ('ASE', 'Administrative and Staff Exchange'), ('EM', 'Executive Meetings')], max_length=4),
        ),
    ]