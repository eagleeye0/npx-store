from django.shortcuts import render
# from control.models import Product


def home(request):
    return render(request, 'index.html')

def not_found(request, any):
    return render(request, '404.html')