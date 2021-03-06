# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-25 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticscanners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencycheck_scan_db',
            name='SEVERITY_HIGH',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dependencycheck_scan_db',
            name='SEVERITY_LOW',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dependencycheck_scan_db',
            name='SEVERITY_MEDIUM',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='findbugs_scan_db',
            name='SEVERITY_HIGH',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='findbugs_scan_db',
            name='SEVERITY_LOW',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='findbugs_scan_db',
            name='SEVERITY_MEDIUM',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retirejs_scan_db',
            name='SEVERITY_HIGH',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retirejs_scan_db',
            name='SEVERITY_LOW',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='retirejs_scan_db',
            name='SEVERITY_MEDIUM',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
