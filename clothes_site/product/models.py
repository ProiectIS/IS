# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import random,os
# Create your models here.

def get_filename_ext(filepath):
     base_name = os.path.basename(filepath)
     name, ext = os.path.splitext(base_name)
     return name, ext

def upload_image_path(self,instance,filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename = new_filename,
            final_filename = final_filename
            )
GENDER_CHOICES = ( ('M','Male'), ('F', 'Female'))
SIZE_CHOICES = (('XS','XS'),('S','S'),('M','M'),('L','L'))
CLOTHES_CHOICES=(('Shirt','Shirts'),('Dress','Dresses'),('Sweater','Sweaters'),('Coat','Coat&Jackets'),('Jeans','Jeans'),('Skirt','Skirts'),('Shoes','Shoes'))
class Product(models.Model):
    category = models.CharField(choices=CLOTHES_CHOICES,max_length=20)
    name = models.CharField(max_length=50)
    productID=models.AutoField(primary_key=True)
    sex=models.CharField(max_length=10,choices=GENDER_CHOICES)
    amount=models.IntegerField()
    price=models.FloatField()
    size=models.CharField(max_length=2,choices=SIZE_CHOICES)  #check-> must be XS/S/M...
    description=models.TextField()
    image=models.ImageField(upload_to='product_photo',blank=True)

    def __str__(self):  #how to print it
        return self.name


