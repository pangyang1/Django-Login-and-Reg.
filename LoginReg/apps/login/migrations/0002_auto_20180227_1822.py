# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]