import pytest
from coffeapi.level0.domain import CoffeShop

@pytest.fixture
def coffeshop(mocker):
    cs  = CoffeShop()
    mocker.patch('coffeapi.level0.views.coffeshop', cs)

    return cs

def test_get(client, coffeshop):
    url = '/PlaceOrder?coffe=coffe&size=size&milk=milk&location=location'
    response = client.get(url)

    assert len(coffeshop.orders) == 1
    assert b'Order=1' == response.content

def test_post(client, coffeshop):
    url = '/PlaceOrder?coffe=coffe&size=size&milk=milk&location=location'
    response = client.get(url)

    assert len(coffeshop.orders) == 1
    assert b'Order=1' == response.content