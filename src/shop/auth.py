from django.shortcuts import redirect, render
from control.models import Customer
import jwt

SECRET_KEY = 'abcd_secret'

def is_login(request):
    token = request.COOKIES.get('token')
    if not token:
        return False

    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
    except Exception:
        return False   

    return True

def get_username(request):
    token = request.COOKIES.get('token')
    if not token:
        return None

    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
    except Exception:
        return None   

    email = jwt.decode(token, 'secret', algorithms=['HS256'])['email']
    return Customer.objects.filter(email=email).first().first_name

def authenticate(request):
    token = request.COOKIES.get('token')
    if not token:
        return False

    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
    except Exception:
        return False   

    return True

def login_user(request):
    # import ipdb; ipdb.set_trace()
    email = request.POST.get('email')
    password = request.POST.get('password')
    customer = Customer.objects.filter(email=email).first()
    if not customer:
        return {'error': 'User does not exist'}

    if customer.password == password:
        token = jwt.encode({'email': email}, 'secret', algorithm='HS256')
        return {'token': token}

    return {'error': 'Invalid credentials'}


def register_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    
    customer = Customer.objects.filter(email=email)
    if customer:
        return {'error': 'User already exists'}

    customer = Customer.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )
    customer.save()

    return login_user(request)



def login(request):
    if request.method == 'GET':
        context = {
            'login_error': request.GET.get('login_error')
        }
        return render(request, 'login.html', context)

    if request.method == 'POST':
        error = None
        auth_login = login_user(request)

        if(auth_login.get('error')):
            # error while logging in
            error = auth_login.get('error')
            return redirect('/login?login_error=' + error)

        else:
            # logged in successfully
            response = redirect('/shop')
            response.set_cookie('token', auth_login.get('token'))
            return response


def register(request):
    if request.method == 'GET':
        context = {
            'register_error': request.GET.get('register_error')
        }
        return render(request, 'register.html', context)

    if request.method == 'POST':
        error = None
        register_user = register_user(request)

        if(register_user.get('error')):
            error = register_user.get('error')
            return redirect('/register?register_error=' + error)

        else:
            response = redirect('/shop')
            response.set_cookie('token', register_user.get('token'))
            return response

def logout(request):
    response = redirect('/login')
    response.delete_cookie('token')
    return response
