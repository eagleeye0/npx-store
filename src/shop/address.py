from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from control.models import CustomerAddress


def get_addresses(request):
    if request.method == 'POST':
        address_count = CustomerAddress.objects.count()
        addresses = CustomerAddress.objects.all()
        address_list_dict = [address for address in addresses.values()]
        response = JsonResponse({
            'addresses': address_list_dict,
        })
        return response
    return HttpResponseBadRequest('method not allowed')
