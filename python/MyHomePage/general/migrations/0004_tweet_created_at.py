# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-21 14:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20160721_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 21, 14, 5, 8, 292165, tzinfo=utc), verbose_name='投稿日'),
            preserve_default=False,
        ),
    ]
