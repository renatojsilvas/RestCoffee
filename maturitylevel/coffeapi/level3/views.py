from coopy.base import init_persistent_system
from coffeapi.level3.domain import CoffeShop, Order, Status
from coffeapi.level3.framework import MyResponse, NoContent, Ok, Created, abs_reverse, allow, datarequired, serialize

coffeshop = init_persistent_system(CoffeShop(), basedir='data/level3')

def order_links(request, order):
    link_to_self = abs_reverse(request, 'order', args=(order.id,))
    
    links = {}
    if order.is_placed():    
        links.update(
            self=link_to_self,
            update=link_to_self,
            cancel=link_to_self,
            payment=abs_reverse(request, 'payment', args=(order.id,))
        )
    elif order.is_paid():
        links.update(
            self=link_to_self,
        )
    elif order.is_served():
        links.update(
            self=link_to_self,
            receipt=abs_reverse(request, 'receipt', args=(order.id,))
        )    

    return links  


@allow('GET', 'POST', 'PUT', 'DELETE')
def dispatch(request, *args, **kwargs):
    methods = dict(GET=read, POST=create, PUT=update, DELETE=delete)
    view = methods[request.method]

    return view(request, *args, **kwargs)

@allow('POST')
@datarequired('coffe', 'size', 'milk', 'location')
def create(request, params=None):     
    
    order = Order(**params, status=Status.Placed)
    coffeshop.place_order(order)  

    d = order.vars()
    d['links'] = order_links(request, order)   

    return Created(
        serialize(d), 
        headers={'Location': abs_reverse(request, 'order', args=(order.id,)) }
        )

@allow('DELETE')
def delete(request, id):           
    
    coffeshop.delete(id=id)

    return NoContent()

@allow('PUT')
@datarequired('coffe', 'size', 'milk', 'location')
def update(request, id, params=None):     
    
    order = Order(id=id, **params)
    coffeshop.update(order)

    d = order.vars()
    d['links'] = order_links(request, order)   

    return Ok(serialize(d))

@allow('GET')
def read(request, id):

    order = coffeshop.read(id=id)     

    d = order.vars()
    d['links'] = order_links(request, order)    

    return MyResponse(serialize(d))

@allow('PUT')
@datarequired('amount')
def payment(request, id, params=None):
    order = coffeshop.pay(id, **params)    

    d = {'links': order_links(request, order)}
   
    return Ok(serialize(d))

def receipt(request, id):
    coffeshop.deliver(id=id)

    return NoContent()