from django.shortcuts import redirect, render
from control.models import Cart


def _cart_id(request):
    session_id = request.session.session_key
    if not session_id:
        session_id = request.session.create()
    return session_id

def add_to_cart(request):
    product_id = request.GET['product_id']
    quantity = int(request.GET['quantity'])
    session_id = _cart_id(request)
    # import ipdb;ipdb.set_trace()
    try:
        cart_item = Cart.objects.get(session_id=session_id,product_id=product_id)
        if quantity == 0 or cart_item.quantity + quantity <= 0:
            cart_item.delete()
        else:
            cart_item.quantity += quantity
            cart_item.save()
    except Cart.DoesNotExist:
        cart_item = Cart.objects.create(
            session_id=session_id,
            product_id=product_id,
            quantity=quantity,
        )
        cart_item.save()
    return redirect('/cart')


def cart(request):
    cart_items = Cart.objects.filter(session_id=_cart_id(request))
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)