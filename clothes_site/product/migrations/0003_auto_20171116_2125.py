# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='name',
            field=models.CharField(default='Shirts', max_length=30),
        ),
    ]
