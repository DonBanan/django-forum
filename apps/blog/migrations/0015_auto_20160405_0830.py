# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 02:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160402_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalmessage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personalmessage_user', to=settings.AUTH_USER_MODEL, verbose_name='\u042e\u0437\u0435\u0440'),
        ),
    ]
