# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontakt', '0006_kontakt_data_urodzenia'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontakt',
            name='jest_adminem',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]