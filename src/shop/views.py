from django.http import HttpResponse, JsonResponse

from control.models import Product


def home(request):
    return HttpResponse('Connected')


def all_products(request):
    products = Product.objects.all()
    product_list_dict = [product for product in products.values()]
    response = JsonResponse({'products': product_list_dict})
    return response


def product(request, product_id):
    product_dict = Product.objects.get(id=product_id).__dict__
    return_dict = {key: product_dict[key] for key in [
        'id', 'product_name', 'mrp_price', 'sale_price']}
    return JsonResponse(return_dict)
