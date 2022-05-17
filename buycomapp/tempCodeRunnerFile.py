from wsgiref.util import request_uri
from django.contrib import messages
from unicodedata import category
from django.http import HttpRequest
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):

    catego=category_choices
    categories_value=[]
    for i in catego:
        for j in i:
            categories_value.append(j)
            break

    obj1=product.objects.all()

    return render(request,'index.html',{'product':obj1,'Categories':categories_value})

def shop(request,type):
    main=product.objects.all()
    url = request.build_absolute_uri()
    print(url.split("/"))
    type=['Smartphone','SmartTv','Laptop','Headphone','SmartWatch','Camera','Speaker']
    for i in type:
        obj1=product.objects.filter(category=i)
    print(obj1)
    return render(request,'shop.html',{'all':obj1,'main':main})

def product_detail(request,pk):

    item=product.objects.get(id=pk)

    return render(request,'detail.html',{'item':item})

def mycart(request):
    return render(request,'cart.html',{})

def checkout(request):
    return render(request,'checkout.html',{})

def contact(request):
    return render(request,'contact.html',{})