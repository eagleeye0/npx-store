from django.shortcuts import render
# from control.models import Product


# Create your views here.
def shop(request):
    # products = Product.objects.all()
    context = {
        # 'products': products
    }
    return render(request, 'shop.html', context)

def product(request, product_id):
    print(product_id)
    return render(request, 'product.html')