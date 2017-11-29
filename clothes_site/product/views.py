# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Product
from django.shortcuts import render

# Create your views here.
def myView(request):
    query_results = Product.objects.all()
    return render(request, 'product/prodTable.html', locals())