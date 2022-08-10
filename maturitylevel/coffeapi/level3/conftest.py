import pytest
import pytest_django
from coffeapi.level3.framework import APIClient

from coffeapi.level3.domain import CoffeShop, Order, Status

@pytest.fixture
def coffeshop(mocker):
    cs  = CoffeShop()
    mocker.patch('coffeapi.level3.views.coffeshop', cs)
    return cs

@pytest.fixture
def order():
    return Order(coffe='latte', size='large', milk='whole', location='takeAway', status=Status.Placed)    

@pytest.fixture
def onecoffee(coffeshop, order):
    coffeshop.place_order(order)
    return coffeshop

@pytest.fixture
def apiclient():
    pytest_django.lazy_django.skip_if_no_django()

    return APIClient()

@pytest.fixture(autouse=True)
def fixed_now(monkeypatch):
    from coffeapi.level3 import domain
    from datetime import datetime
    monkeypatch.setattr(domain, 'now', lambda: datetime(2021, 4, 28))
