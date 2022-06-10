# from control.models import Cart, Customer
# from shop import auth
# # from shop.apis import cart_items_number
# from shop.cart import _cart_id, cart
# from django.db.models import Sum


# def cart_detail(request):
#     if auth.is_login(request):
#         customer_id = auth.get_customer_id(request)
#         cart_items = Cart.objects.filter(customer_id=customer_id)
#         cart_items_number = cart_items.aggregate(Sum('quantity'))[
#             'quantity__sum']

#     else:
#         cart_items_number = Cart.objects.filter(session_id=_cart_id(
#             request)).aggregate(Sum('quantity'))['quantity__sum']

#     return {'cart_items_number': cart_items_number}


# def login_detail(request):
#     if auth.is_login(request):
#         return {'is_login': True, 'username': auth.get_name(request)}
#     else:
#         return {'is_login': False}
