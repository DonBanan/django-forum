# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20160407_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='moderated',
            field=models.BooleanField(default=False, verbose_name='\u041d\u0430 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0435 \u043c\u043e\u0434\u0435\u0440\u043e\u043c'),
        ),
        migrations.AlterField(
            model_name='moderated',
            name='moderated',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u043b \u043c\u043e\u0434\u0435\u0440\u0430\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f'),
        ),
    ]
