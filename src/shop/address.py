from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse

from control.models import CustomerAddress
from shop.auth import token_required


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


@token_required
def add_address(request, user_id):
    if request.method == "POST":
        address_line_1 = request.POST.get('address_line_1')
        address_line_2 = request.POST.get('address_line_2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        address_type = request.POST.get('address_type')

        new_address = CustomerAddress.objects.create(
            customer_id=user_id,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state=state,
            pincode=pincode,
            address_type=address_type,
        )
        
        new_address.save()

        return HttpResponse('success')

@token_required
def delete_address(request, user_id):
    if request.method == "POST":
        import ipdb; ipdb.set_trace()
        try:
            address_type = request.POST.get('address_type')
            address = CustomerAddress.objects.get(customer_id=user_id, type=address_type)
            address.delete()
            return HttpResponse("success")
        except:
            return HttpResponseNotFound("Address not found")