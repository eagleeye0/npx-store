

from control.models import Cart
from shop import auth
# from shop.apis import cart_items_number
from shop.cart import _cart_id, cart
from django.db.models import Sum


def cart_detail(request):
    cart_items_number = Cart.objects.filter(session_id=_cart_id(request)).aggregate(Sum('quantity'))['quantity__sum']
    return {'cart_items_number': cart_items_number}

def login_detail(request):
    if auth.is_login(request):
        return {'is_login': True, 'username': auth.get_username(request)}
    else:
        return {'is_login': False}