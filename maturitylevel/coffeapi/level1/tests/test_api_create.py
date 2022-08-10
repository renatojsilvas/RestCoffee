from http import HTTPStatus
from coffeapi.level1.domain import CoffeShop

def test_get_not_allowed(client, coffeshop):
    url = '/order/create?coffe=latte&size=large&milk=whole&location=takeAway'
    response = client.get(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeshop.orders) == 0

def test_post_success(client, coffeshop):
    url = '/order/create?coffe=latte&size=large&milk=whole&location=takeAway'
    response = client.post(url)

    assert response.status_code == HTTPStatus.CREATED
    assert len(coffeshop.orders) == 1
    assert response.content == b'coffe=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large'

def test_post_badrequest(client, coffeshop):
    url = '/order/create?coffe=latte&size=large&milk=whole'
    response = client.post(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(coffeshop.orders) == 0    