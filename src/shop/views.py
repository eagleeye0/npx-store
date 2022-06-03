from django.shortcuts import redirect, render

from shop import auth
from . import apis
from control.models import Product
import json



def home(request):
    return render(request, 'index.html')

def shop(request):
    products = Product.objects.all()
    context = {}
    context = context | {'products': products}
    response = render(request, 'shop.html', context)
    return response

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product.html', context)

