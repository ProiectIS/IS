# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from product.models import Product
# Create your views here.
def shirtView(request):
    all_prod=Product.objects.all()
    all_shirts=all_prod.filter(category="Shirt")
    template=loader.get_template('shirts/shirts.html')
    context={'all_shirts':all_shirts}
    return HttpResponse(template.render(context,request))

def shirtDetail(request,shirt_id):
    all_prod = Product.objects.all()
    all_shirts = all_prod.filter(category="Shirt")
    template=loader.get_template('shirts/detail.html')
    myShirt=all_shirts.get(productID=shirt_id)
    context={'myShirt':myShirt}
    return HttpResponse(template.render(context,request))