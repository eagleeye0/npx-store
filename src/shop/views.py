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

def login(request):
    if request.method == 'GET':
        context = {
            'login_error': request.GET.get('login_error')
        }
        return render(request, 'login.html', context)

    if request.method == 'POST':
        error = None
        login_user = auth.login_user(request)

        if(login_user.get('error')):
            # error while logging in
            error = login_user.get('error')
            return redirect('/login?login_error=' + error)

        else:
            # logged in successfully
            response = redirect('/shop')
            response.set_cookie('token', login_user.get('token'))
            return response


def register(request):
    if request.method == 'GET':
        context = {
            'register_error': request.GET.get('register_error')
        }
        return render(request, 'register.html', context)

    if request.method == 'POST':
        error = None
        register_user = auth.register_user(request)

        if(register_user.get('error')):
            error = register_user.get('error')
            return redirect('/register?register_error=' + error)

        else:
            response = redirect('/shop')
            response.set_cookie('token', login_user.get('token'))

def logout(request):
    response = redirect('/login')
    response.delete_cookie('token')
    return response