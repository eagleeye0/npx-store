from django.shortcuts import redirect, render
from . import apis
# from control.models import Product


def home(request):
    return render(request, 'index.html')


def shop(request):
    # import ipdb; ipdb.set_trace()
    # products = Product.objects.all()
    context = {}
    context = context | apis.get_header_detail(request)
    response = render(request, 'shop.html', context)
    # response.set_cookie("token", "verygoodtoken")
    return response


def product(request, product_id):
    print(product_id)
    return render(request, 'product.html')


def cart(request):
    return render(request, 'cart.html')


def login(request):
    if request.method == 'GET':
        context = {
            'login_error': request.GET.get('login_error')
        }
        return render(request, 'login.html', context)

    if request.method == 'POST':
        error = None
        login_user = apis.login_user(request)
        if(login_user.get('error')):
            error = login_user.get('error')
        else:
            response = redirect('/shop')
            response.set_cookie('token', login_user.get('token'))

        if error:
            response = redirect('/login?login_error=' + error)
        return response


def register(request):
    if request.method == 'GET':
        context = {
            'register_error': request.GET.get('register_error')
        }
        return render(request, 'login.html', context)

    if request.method == 'POST':
        error = None
        register_user = apis.register_user(request)
        if(register_user.get('error')):
            error = register_user.get('error')
        else:
            login_user = apis.login_user(request)
            if(login_user.get('error')):
                error = login_user.get('error')
            else:
                response = redirect('/shop')
                response.set_cookie('token', login_user.get('token'))

        if error:
            response = redirect('/register?register_error=' + error)
        return response

