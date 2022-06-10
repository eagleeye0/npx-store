from django.shortcuts import redirect, render
from control.models import Cart, Customer
from shop import auth


def _session_id(request):
    session_id = request.session.session_key
    if not session_id:
        session_id = request.session.create()
    return session_id

def add_to_cart(request):
    product_id = request.GET['product_id']
    quantity = int(request.GET['quantity'])
    if auth.is_login(request):
        # import ipdb; ipdb.set_trace()
        email = auth.get_email(request)
        customer_id = Customer.objects.get(email=email).id
        try:
            cart_item = Cart.objects.get(customer_id=customer_id, product_id=product_id)
        # if cart_item:
            if quantity == 0 or cart_item.quantity + quantity <= 0:
                cart_item.delete()
            else:
                cart_item.quantity = cart_item.quantity + quantity
                cart_item.save()
        except:
            if quantity > 0:
                Cart.objects.create(customer_id=customer_id, product_id=product_id, quantity=quantity)
        return redirect('/cart')

    else:
        session_id = _session_id(request)
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
    if auth.is_login(request): 
        customer_id = auth.get_customer_id(request)
        cart_items = Cart.objects.filter(customer_id=customer_id)
    else:
        cart_items = Cart.objects.filter(session_id=_session_id(request))
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)

def login_required(request,next_url=None, *args2):
    if auth.is_login(request):
        return redirect(next_url)
    else:
        return auth.login(request, next_url)

def checkout(request):
    if auth.is_login(request):
        customer_id = auth.get_customer_id(request)
        cart_items = Cart.objects.filter(customer_id=customer_id)
        context = {'cart_items': cart_items}
        return render(request, 'checkout.html', context)
    else:
        return redirect('/login')