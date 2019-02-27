# ----------------------------------------------------------------------------
# Copyright (c) 2016-2019, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0014_option_workshop_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billed_datetime',
            field=models.CharField(
                blank=True, default='',
                help_text='This is the confirmed date and time of payment',
                max_length=300, verbose_name='billed date & time'),
            preserve_default=False,
        ),
    ]
