# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
import random,os
from django.contrib.auth.models import User



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

MY_CHOICES = (
    ('Female', (
        ('Shirt', 'Shirts'), ('Dress', 'Dresses'), ('Sweater', 'Sweaters'), ('Coat', 'Coat&Jackets'),
        ('Jeans', 'Jeans'), ('Skirt', 'Skirts')
        )
    ),
    ('Male', (
        ('Tshirts', 'Tshirts'), ('Hoodies', 'Hoodies'), ('MJeans', 'Jeans'), ('MCoats', 'Coats')
        )
    ),
)
class Product(models.Model):
    category = models.CharField(choices=MY_CHOICES,max_length=20)
    name = models.CharField(unique=True,max_length=50)
    productID=models.AutoField(primary_key=True)
    price=models.FloatField()
    size_XS_amount= models.PositiveIntegerField()
    size_S_amount = models.PositiveIntegerField()
    size_M_amount = models.PositiveIntegerField()
    size_L_amount = models.PositiveIntegerField()
    description=models.TextField()
    image=None

    def __str__(self):  #how to print it
        return self.name

class Image(models.Model):
    product=models.ForeignKey(Product)
    image=models.ImageField(upload_to='product_photo', blank=True)

    def __str__(self):
        return str(self.product)+' '+str(self.image)

class Customer(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    #phone=models.CharField(max_length=12)
    #address=models.CharField(max_length=100)
    password=models.CharField(max_length=20)

    def __str__(self):  #how to print it
       return self.first_name

    def get_absolute_url(self):
        return reverse('mainapp:profile',kwargs={'id':self.pk})  #to reach the profile page of the customer

#TO DO: add address + phone

