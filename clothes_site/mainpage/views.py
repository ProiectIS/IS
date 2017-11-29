# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Mainpage

# Create your views here.
def first_page(request):
    page=Mainpage.objects.get()
    return render(request,'mainpage/main.html',{'page':page})