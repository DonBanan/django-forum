# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20160406_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='count_views',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u043e\u0432'),
        ),
    ]
