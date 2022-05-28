from django.shortcuts import render
from control.models import Product


def home(request):
    return render(request, 'index.html')
