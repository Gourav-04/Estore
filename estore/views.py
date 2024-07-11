from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from math import ceil

def home(request):
    # products=Product.objects.all()
    allProducts=[]
    category= Product.objects.values('category')
    print(category)
    unique_category={item['category'] for item in category}

    for cat in unique_category:
        product=Product.objects.filter(category=cat)
        no_of_products=len(product)
        no_of_slides=(no_of_products)//4 + ceil(no_of_products/4 - no_of_products//4)
        allProducts.append([no_of_products,product,range(1,no_of_slides),no_of_slides])
    params={"allProducts":allProducts}
    return render(request,"estore/index.html",params)

def about(request):
    return render(request,"estore/about.html")

def contact(request):
    return render(request,"estore/contact.html")

def tracker(request):
    return render(request,"estore/tracker.html")

def search(request):
    return render(request,"estore/search.html")

def productView(request):
    return render(request,"estore/productView.html")

def checkout(request):
    return render(request,"estore/checkout.html")


