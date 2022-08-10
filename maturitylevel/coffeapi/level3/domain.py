
from datetime import datetime
from decimal import Decimal
from enum import Enum, auto

def now():
    from django.utils.datetime_safe import datetime 
    return datetime.now()

class Status(Enum):
    Placed = auto()
    Paid = auto() 
    Served = auto()
    Collected = auto()
    Cancelled = auto()

class DoesNotExist(Exception):
    pass

O_PATRAO_ESTA_MALUCO = Decimal('1.99')

class Order:
    def __init__(self, coffe='', size='', milk='', location='', id = None, created_at=None, status=None) -> None:
        self.id = None if id is None else int(id)
        self.coffe = coffe
        self.size = size
        self.milk = milk
        self.location = location
        self.created_at = now() if created_at is None else created_at
        self.status = status
        self.price = O_PATRAO_ESTA_MALUCO

    def vars(self):
        d = vars(self).copy()
        d['status'] = str(d['status']).removeprefix('Status.')
        del d['price']
        return d

    def is_cancelled(self):
        return self.status == Status.Cancelled

    def is_paid(self):
        return self.status == Status.Paid

    def is_collected(self):
        return self.status == Status.Collected
    
    def is_placed(self):
        return self.status == Status.Placed
    
    def is_served(self):
        return self.status == Status.Served


class Conflicted(Exception):
    pass

class CoffeShop:
    def __init__(self) -> None:
        self.orders = {}    

    def place_order(self, order):
        if order.id is None:
            order.id = len(self.orders) + 1
        self.orders[order.id] = order
        return order 

    def delete(self, id):
        id = int(id)
        try:
            order = self.orders[id]           
        except KeyError as e:        
            raise DoesNotExist(id) 
        
        order.status = Status.Cancelled            
        return order

    def update(self, order):
        saved = self.read(order.id)

        if order.status is None:
            order.status = saved.status
            
        self.orders[order.id] = order
        return order

    def read(self, id):    
        id = int(id)
        try:    
            return self.orders[id]
        except KeyError as e:        
            raise DoesNotExist(id)    

    def pay(self, id, amount):
        amount= Decimal(amount) / 100
        order = self.read(id=id)  

        if order.is_paid():
            raise Conflicted(id)

        if amount == order.price:
            order.status = Status.Paid   
        return order  

    def deliver(self, id):
        order = self.read(id)

        if order.is_collected():
            raise Conflicted(id)     

        order.status = Status.Collected
        return order

    def ready(self, id):
        order = self.read(id)

        if order.is_paid():
            raise Conflicted(id)     

        order.status = Status.Served
        return order