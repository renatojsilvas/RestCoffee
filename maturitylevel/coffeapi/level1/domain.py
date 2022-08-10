class DoesNotExist(Exception):
    pass

class Order:
    def __init__(self, coffe='', size='', milk='', location='', id = None) -> None:
        self.id = None if id is None else int(id)
        self.coffe = coffe
        self.size = size
        self.milk = milk
        self.location = location

    def __str__(self):
        return '\n'.join((f'{k}={v}' for k, v in sorted(vars(self).items())))

class CoffeShop:
    def __init__(self) -> None:
        self.orders = {}    

    def place_order(self, order):
        if order.id is None:
            order.id = len(self.orders) + 1
        self.orders[order.id] = order
        return order 

    def delete(self, order):
        try:
            return self.orders.pop(order.id)   
        except KeyError as e:
            raise DoesNotExist(order.id)

    def update(self, order):
        if order.id not in self.orders:
            raise DoesNotExist(order.id) 

        self.orders[order.id] = order
        return order

    def read(self, id):    
        id = int(id)
        try:    
            return self.orders[id]
        except KeyError as e:        
            raise DoesNotExist(id)         