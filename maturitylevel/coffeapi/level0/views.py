
from coopy.base import init_persistent_system
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from coffeapi.level0.domain import CoffeShop, Order

coffeshop = init_persistent_system(CoffeShop(), basedir='data/level0/')

def barista(request):
    """
    http://127.0.0.1:8000/PlaceOrder/?coffe=coffe&size=.size&milk=milk&location=location
    - Erro com status code 200. Trocar para Badrequest.
    - Get com efeito colateral.
    - Impossível de cachear.
    """

    try:
        params = {k: request.GET[k]
                  for k in ('coffe', 'size', 'milk', 'location')}
    except MultiValueDictKeyError:
        body = 'Erro não possível registrar o pedido.'
        header = { 'Content-Type': 'text/plain; charset=utf-8'}
        return HttpResponse(body, headers=header)
    
    order = Order(**params)
    coffeshop.place_order(order)
    
    body = f'Order={order.id}'
    header = { 'Content-Type': 'text/plain; charset=utf-8' }

    return HttpResponse(body, headers=header)
