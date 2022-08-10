
from coopy.base import init_persistent_system
from django.urls import reverse

from coffeapi.level2.domain import CoffeShop, Order, Status
from coffeapi.level2.framework import MyResponse, NoContent, Created, abs_reverse, allow, datarequired, serialize

coffeshop = init_persistent_system(CoffeShop(), basedir='data/level2')

@allow('GET', 'POST', 'PUT', 'DELETE')
def dispatch(request, *args, **kwargs):
    methods = dict(GET=read, POST=create, PUT=update, DELETE=delete)
    view = methods[request.method]

    return view(request, *args, **kwargs)

@allow('POST')
@datarequired('coffe', 'size', 'milk', 'location')
def create(request, params=None):     
    
    order_old = Order(**params, status=Status.Placed)
    coffeshop.place_order(order_old)    

    return Created(
        serialize(order_old), 
        headers={'Location': abs_reverse(request, 'order_old', args=(order_old.id,)) }
        )

@allow('DELETE')
def delete(request, id):        
    
    order_old = Order(id=id)
    coffeshop.delete(order_old)

    return NoContent()

@allow('PUT')
@datarequired('coffe', 'size', 'milk', 'location')
def update(request, id, params=None):     
    
    order_old = Order(id=id, **params)
    coffeshop.update(order_old)

    return NoContent()

@allow('GET')
def read(request, id):

    order_old = coffeshop.read(id=id)     

    return MyResponse(serialize(order_old))

