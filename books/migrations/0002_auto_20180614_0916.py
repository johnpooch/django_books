# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/default-image.jpg', upload_to='images'),
        ),
    ]
