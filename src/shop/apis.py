

import django
from django.http import JsonResponse
from control.models import Cart, Customer


def get_header_detail(request):
    context = {}
    context = context | cart_items_number(request)
    return context


def is_login(request):
    if request.user.is_authenticated:
        return {'is_login': True}

    return {'is_login': False}


def get_cart_content(request):
    cart = Cart.objects.filter(user=request.user)
    return cart


def cart_items_number(request):
    # TODO: check if user is logged in
    # if request.user.is_authenticated:
    #     cart = Cart.objects.filter(user=request.user)
    #     if cart.exists():
    #         return cart[0].items.count()
    return {'cart_items_number': 5}


def login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    customer = Customer.objects.filter(email=email).first()
    if not customer:
        return {'error': 'user does not exist'}

    if customer.password == password:
        # generate jwt_token
        return {'token': email}

    return {'error': 'invalid credentials'}


def register_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    phone = request.POST.get('phone')
    customer = Customer.objects.filter(email=email)
    if customer:
        return {'error': 'user already exists'}

    customer = Customer.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        phone=phone,
    )
    customer.save()
    return {}

