from django.shortcuts import redirect, render
# from control.models import Product


def shop(request):
    # products = Product.objects.all()
    context = {
        # 'products': products
    }
    return render(request, 'shop.html', context)

def product(request, product_id):
    print(product_id)
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        # login user
        return redirect('/shop')

def register(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        # register user
        return redirect('/shop')
