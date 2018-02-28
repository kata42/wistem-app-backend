# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20180228_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='applicanttype',
            field=models.ManyToManyField(blank=True, to='api.Applicanttype'),
        ),
        migrations.AlterField(
            model_name='award',
            name='awardpurpose',
            field=models.ManyToManyField(blank=True, to='api.Awardpurpose'),
        ),
        migrations.AlterField(
            model_name='award',
            name='stemfield',
            field=models.ManyToManyField(blank=True, to='api.Stemfield'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='areasofinterest',
            field=models.ManyToManyField(blank=True, to='api.Areaofinterest'),
        ),
    ]
