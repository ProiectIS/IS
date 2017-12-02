# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mainapp.models import Product,Image,Customer

# Register your models here.
#admin.site.register(Product)


class InlineImage(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Product, ProductAdmin)