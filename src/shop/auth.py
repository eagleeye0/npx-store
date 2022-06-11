from datetime import datetime, timedelta, timezone
import math
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from control.models import Cart, Customer
import jwt
from django.contrib.auth.hashers import make_password, check_password
from credentials import JWT_SECRET
from django.views.generic import TemplateView

from django import forms


SECRET_KEY = JWT_SECRET

def authenticate_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

class Login(TemplateView):
    def post(self, request):
        # import ipdb; ipdb.set_trace()
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return HttpResponseBadRequest('Missing email or password')

        customer = Customer.objects.filter(email=email).first()

        if not customer:
            return HttpResponseBadRequest('User does not exist')

        if check_password(password, customer.password):
            # import ipdb; ipdb.set_trace()
            token = jwt.encode({'email': email, 'id': customer.id, 'exp': datetime.now(
                tz=timezone.utc) + timedelta(days=7)}, SECRET_KEY, algorithm='HS256')
            customer_dict = customer.__dict__
            return_dict = {key: customer_dict[key] for key in [
                'id', 'email']}
            response = JsonResponse({'user': return_dict})
            response.set_cookie('jwttoken', token,
                                max_age=60 * 60 * 24 * 7, httponly=True)
            return response

        return HttpResponseForbidden('Invalid credentials')


class Register(TemplateView):
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_pwd = make_password(password)

        if not email or not password:
            return HttpResponseBadRequest('Missing email or password')

        customer = Customer.objects.filter(email=email)
        if customer:
            return HttpResponseBadRequest('User already exists')

        customer = Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_pwd,
        )
        customer.save()
        return HttpResponse('Success')

def me(request):
    # import ipdb; ipdb.set_trace()
    if request.method == "GET":
        user_id = authenticate_token(request.COOKIES.get('jwttoken'))
        if not user_id:
            return HttpResponseBadRequest('Invalid token')

        customer = Customer.objects.get(id=user_id).__dict__
        return_dict = {your_key: customer[your_key] for your_key in [
            'id', 'first_name', 'last_name', 'email']}
        return JsonResponse(return_dict)

class Logout(TemplateView):
    def get(self, request):
        response = HttpResponse('Success')
        response.delete_cookie('jwttoken')
        return response


def get_customer(request, customer_id):
    if request.method == "GET":
        customer = Customer.objects.get(id=customer_id).__dict__
        return_dict = {your_key: customer[your_key] for your_key in [
            'id', 'first_name', 'last_name', 'email']}
        return JsonResponse(return_dict)

    return HttpResponseBadRequest('method not allowed')


def generateOTP():
    digits = "123456789"
    OTP = ""

    import random
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


def reset_password_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if not email:
            return HttpResponseBadRequest('Missing email')

        customer = Customer.objects.filter(email=email).first()
        if not customer:
            return HttpResponseBadRequest('User does not exist')

        otp = generateOTP()
        customer.reset_otp = otp
        customer.save()
        return HttpResponse('Success')

    return HttpResponseBadRequest('method not allowed')


def reset_password_using_otp(request):
    # import ipdb; ipdb.set_trace()
    if request.method == "POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        password = request.POST.get('password')
        if not otp or not email:
            return HttpResponseBadRequest('Missing field')

        customer = Customer.objects.filter(email=email).first()
        if not customer:
            return HttpResponseBadRequest('User does not exist')

        if otp == customer.reset_otp:
            customer.reset_otp = None
            customer.password = make_password(password)
            customer.save()
            return HttpResponse('Success')

        return HttpResponseBadRequest('Invalid OTP')

    return HttpResponseBadRequest('method not allowed')


def update_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        if not email or not password or not new_password:
            return HttpResponseBadRequest('Missing field')

        customer = Customer.objects.filter(email=email).first()
        if not customer:
            return HttpResponseBadRequest('User does not exist')

        if check_password(password, customer.password):
            customer.password = make_password(new_password)
            customer.save()
            return HttpResponse('Success')

        return HttpResponseBadRequest('Invalid credentials')
