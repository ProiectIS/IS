# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path),
        ),
    ]