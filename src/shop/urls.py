# from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views, cart
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>', views.product, name='product'),
    path('cart/', cart.cart, name='cart'),
    path('add-to-cart/', cart.add_to_cart, name='add-to-cart'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
