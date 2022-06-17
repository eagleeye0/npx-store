import math
import sys
from unicodedata import name
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from control.models import Product, SubscibeList


def home(request):
    return HttpResponse('Connected')


def all_products(request):
    if request.method == 'POST':
        # import ipdb
        # ipdb.set_trace()
        page_number = int(request.POST.get('page_number') or 1)
        page_size = int(request.POST.get('page_size') or 10**8)
        product_count = Product.objects.count()
        products = Product.objects.all()[(
            page_number-1)*page_size:page_number*page_size]
        product_list_dict = [product for product in products.values()]
        response = JsonResponse({
            'products': product_list_dict,
            'product_count': product_count,
            'page_count': math.ceil(product_count/page_size)
        })
        return response
    return HttpResponseBadRequest('method not allowed')


def product(request, product_id):
    product_dict = Product.objects.get(id=product_id).__dict__
    return_dict = {key: product_dict[key] for key in [
        'id', 'product_name', 'mrp_price', 'sale_price']}
    return JsonResponse(return_dict)


def subscribe(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    if email and name:
        subscriber = SubscibeList.objects.create(email=email, name=name)
        subscriber.save()
        return HttpResponse("Success")

    return HttpResponseBadRequest('Missing field')
