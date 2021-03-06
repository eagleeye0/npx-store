# from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

from . import views, cart, auth, address
from django.urls import path


urlpatterns = [
    # test
    path('', views.home, name='home'),
    
    # products
    path('apiv1/all_products/', views.all_products, name='all_products'),
    path('apiv1/product/<int:product_id>', views.product, name='product'),
    
    # address
    path('apiv1/get-addresses/', address.get_addresses, name='get_address'),
    path('apiv1/add-address/', address.add_address, name='add_address'),
    path('apiv1/delete-address/', address.delete_address, name='delete_address'),
    
    # cart
    path('apiv1/get-cart-items/', cart.get_cart_items, name='cart'),
    path('apiv1/update-cart/<int:product_id>/<int:quantity>', cart.update_cart, name='add-to-cart'),
    
    # subscribe list
    path('apiv1/subscribe/', views.subscribe, name='subscribe'),
    
    # login and auth
    path('apiv1/login/', auth.Login.as_view(), name='login'),
    path('apiv1/me/', auth.me, name='me'),
    path('apiv1/register/', auth.Register.as_view(), name='register'),
    path('apiv1/logout/', auth.Logout.as_view(), name='logout'),
    path('apiv1/reset_password_request/', auth.reset_password_request, name='reset_password_request'),
    path('apiv1/reset_password_using_otp/', auth.reset_password_using_otp, name='reset_password_using_otp'),
    path('apiv1/update_password/', auth.update_password, name='update_password'),
    # path('apiv1/get_customer/<int:customer_id>', auth.get_customer, name='get_customer'),
    
    # orders
]
