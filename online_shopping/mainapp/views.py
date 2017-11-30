from __future__ import unicode_literals
from django.shortcuts import render
from mainapp.models import Product,Image
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def first_page(request):
    return render(request,'mainapp/main.html',locals())

def prod_table(request):
    query_results=Product.objects.all()
    return render(request,'mainapp/prodTable.html',locals())

def full_page(category):
    all_images = Image.objects.all()
    all_items = []
    for img in all_images:
        if (img.product.category == category) and (img.product not in all_items):
            img.product.image = img.image
            all_items.append(img.product)
    return all_items

def shirts_page(request):
    all_items = full_page("Shirt")
    template = loader.get_template('mainapp/items.html')
    context = {'all_items': all_items,'name':"shirts",'title':"SHIRTS"}
    return HttpResponse(template.render(context, request))

def dresses_page(request):
    all_items=full_page("Dress")
    template = loader.get_template('mainapp/items.html')
    context = {'all_items': all_items,'name':"dresses",'title':"DRESSES"}
    return HttpResponse(template.render(context, request))

def sweaters_page(request):
    all_items = full_page("Sweater")
    template = loader.get_template('mainapp/items.html')
    context = {'all_items': all_items, 'name': "sweaters", 'title': "SWEATERS"}
    return HttpResponse(template.render(context, request))

def coats_page(request):
    all_items = full_page("Coat")
    template = loader.get_template('mainapp/items.html')
    context = {'all_items': all_items, 'name': "coats&jackets", 'title': "COATS&JACKETS"}
    return HttpResponse(template.render(context, request))

def jeans_page(request):
    all_items = full_page("Jeans")
    template = loader.get_template('mainapp/items.html')
    context = {'all_items': all_items, 'name': "jeans", 'title': "JEANS"}
    return HttpResponse(template.render(context, request))

def skirts_page(request):
    all_items = full_page("Skirt")
    template = loader.get_template('mainapp/items.html')
    context = {'all_items': all_items, 'name': "skirts", 'title': "SKIRTS"}
    return HttpResponse(template.render(context, request))

def shoes_page(request):
    all_items = full_page("Shoes")
    template = loader.get_template('mainapp/items.html')
    context = {'all_items': all_items, 'name': "shoes", 'title': "SHOES"}
    return HttpResponse(template.render(context, request))

#--------------------------------------------------------------------------

def details(request,category,item_id):
    all_prod = Product.objects.all()
    all_images = Image.objects.all()
    all_items = all_prod.filter(category=category)
    my_images = []
    myItem = all_items.get(productID=item_id)
    for img in all_images:
        if (img.product == myItem):
            my_images.append(str(img.image))
    template = loader.get_template('mainapp/details.html')
    context = {'myItem': myItem, 'my_images': my_images}
    return HttpResponse(template.render(context, request))

def shirt_detail(request,shirt_id):
    return details(request,"Shirt",shirt_id)

def dress_detail(request,dress_id):
    return details(request,"Dress", dress_id)

def sweater_detail(request,sweater_id):
    return details(request,"Sweater", sweater_id)

def coat_detail(request,coat_id):
    return details(request,"Coat", coat_id)

def jean_detail(request,jean_id):
    return details(request,"Jeans", jean_id)

def skirt_detail(request,skirt_id):
    return details(request,"Skirt", skirt_id)

def shoe_detail(request,shoe_id):
    return details(request,"Shoes", shoe_id)
