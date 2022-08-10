
from datetime import datetime
from enum import Enum, auto

def now():
    from django.utils.datetime_safe import datetime 
    return datetime.now()

class Status(Enum):
    Placed = auto()
    Paid = auto() 
    Served = auto()
    Collected = auto()

class DoesNotExist(Exception):
    pass

class Order:
    def __init__(self, coffe='', size='', milk='', location='', id = None, created_at=None, status=None) -> None:
        self.id = None if id is None else int(id)
        self.coffe = coffe
        self.size = size
        self.milk = milk
        self.location = location
        self.created_at = now() if created_at is None else created_at
        self.status = status

    def vars(self):
        d = vars(self)
        d['status'] = str(d['status']).removeprefix('Status.')
        return d

class CoffeShop:
    def __init__(self) -> None:
        self.orders = {}    

    def place_order(self, order_old):
        if order_old.id is None:
            order_old.id = len(self.orders) + 1
        self.orders[order_old.id] = order_old
        return order_old 

    def delete(self, order_old):
        try:
            return self.orders.pop(order_old.id)   
        except KeyError as e:
            raise DoesNotExist(order_old.id)

    def update(self, order_old):
        saved = self.read(order_old.id)

        if order_old.status is None:
            order_old.status = saved.status
            
        self.orders[order_old.id] = order_old
        return order_old

    def read(self, id):    
        id = int(id)
        try:    
            return self.orders[id]
        except KeyError as e:        
            raise DoesNotExist(id)         