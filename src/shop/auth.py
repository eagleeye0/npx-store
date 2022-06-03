from control.models import Customer
import jwt


def is_login(request):
    # if jwt.deco
    pass

def authenticate(request):
    token = request.COOKIES.get('token')
    if not token:
        return False

    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return False    

    return True

def login_user(request):
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