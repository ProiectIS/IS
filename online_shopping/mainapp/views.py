from __future__ import unicode_literals
from django.shortcuts import render
from mainapp.models import Product
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def first_page(request):
    return render(request,'mainapp/main.html',locals())

def shirts_page(request):
    all_prod = Product.objects.all()
    all_shirts = all_prod.filter(category="Shirt")
    template = loader.get_template('mainapp/shirts.html')
    context = {'all_shirts': all_shirts}
    return HttpResponse(template.render(context, request))

def shirt_detail(request,shirt_id):
    all_prod = Product.objects.all()
    all_shirts = all_prod.filter(category="Shirt")
    template=loader.get_template('mainapp/shirt_detail.html')
    myShirt=all_shirts.get(productID=shirt_id)
    context={'myShirt':myShirt}
    return HttpResponse(template.render(context,request))

def dresses_page(request):
    all_prod = Product.objects.all()
    all_dresses = all_prod.filter(category="Dress")
    template = loader.get_template('mainapp/dresses.html')
    context = {'all_dresses': all_dresses}
    return HttpResponse(template.render(context, request))

def dress_detail(request,dress_id):
    all_prod = Product.objects.all()
    all_dresses = all_prod.filter(category="Dress")
    template=loader.get_template('mainapp/dress_detail.html')
    myDress=all_dresses.get(productID=dress_id)
    context={'myDress':myDress}
    return HttpResponse(template.render(context,request))