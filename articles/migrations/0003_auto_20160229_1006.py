# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20160229_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comments',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='down',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='up',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
