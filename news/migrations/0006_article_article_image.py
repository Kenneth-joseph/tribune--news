# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-29 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200129_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='kent', upload_to='articles/'),
        ),
    ]
