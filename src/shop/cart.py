from math import prod
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from control.models import Cart, Customer, Product
from shop.auth import token_required


@token_required
def update_cart(request, user_id, product_id, quantity):
    try:
        Product.objects.get(id=product_id)
    except:
        return HttpResponseBadRequest("Product does not exist")

    try:
        # if cart_item
        cart_item = Cart.objects.get(customer_id=user_id, product_id=product_id)
        if quantity == 0:
            cart_item.delete()
        else:
            cart_item.quantity = quantity
            cart_item.save()

    except:
        if quantity > 0:
            Cart.objects.create(customer_id=user_id, product_id=product_id, quantity=quantity)

    return HttpResponse("Success")


@token_required
def get_cart_items(request, user_id):
    cart_items = Cart.objects.filter(customer_id=user_id)
    cart_items_list_dict = [cart_item for cart_item in cart_items.values()]
    response = JsonResponse({
        'products': cart_items_list_dict,
    })
    return response
