from django.shortcuts import render
from control.models import Product


# Create your views here.
def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    print(context)
    return render(request, 'shop.html', context)
