import pytest

from coffeapi.level1.domain import CoffeShop, Order

@pytest.fixture
def coffeshop(mocker):
    cs  = CoffeShop()
    mocker.patch('coffeapi.level1.views.coffeshop', cs)
    return cs

@pytest.fixture
def order():
    return Order(coffe='latte', size='large', milk='whole', location='takeAway')    

@pytest.fixture
def onecoffee(coffeshop, order):
    coffeshop.place_order(order)
    return coffeshop