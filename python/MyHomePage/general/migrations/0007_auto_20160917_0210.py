# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-17 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20160721_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterAccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=110, verbose_name='アクセスキー')),
                ('secret', models.CharField(max_length=100, verbose_name='アクセスシークレット')),
                ('created_at', models.DateTimeField(verbose_name='登録日')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-created_at']},
        ),
    ]
