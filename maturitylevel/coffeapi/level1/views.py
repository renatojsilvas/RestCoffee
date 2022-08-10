from coopy.base import init_persistent_system

from coffeapi.level1.domain import CoffeShop, Order
from coffeapi.level1.framework import MyResponse, NoContent, Created, allow, require, serialize

coffeshop = init_persistent_system(CoffeShop(), basedir='data/level1')

@allow(['POST'])
@require(['coffe', 'size', 'milk', 'location'])
def create(request, params=None):     
    
    order = Order(**params)
    coffeshop.place_order(order)   

    return Created(serialize(order))

@allow(['POST'])
@require(['id'])
def delete(request, params=None):        
    
    order = Order(**params)
    coffeshop.delete(order)

    return NoContent()

@allow(['POST'])
@require(['id', 'coffe', 'size', 'milk', 'location'])
def update(request, params=None):     
    
    order = Order(**params)
    coffeshop.update(order)

    return NoContent()

@allow(['GET'])
@require(['id'])
def read(request, params=None):

    order = coffeshop.read(**params)     

    return MyResponse(serialize(order))

