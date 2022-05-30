

from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>', views.product, name='product'),
]
