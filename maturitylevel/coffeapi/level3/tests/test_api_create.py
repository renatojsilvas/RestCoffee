from datetime import datetime
from http import HTTPStatus
import pytest

from coffeapi.level3.framework import deserialize
from coffeapi.level3.domain import Status

@pytest.mark.skip
def test_get_not_allowed(apiclient, coffeshop):
    url = '/order'
    data = dict(coffe='latte', size='large', milk='whole', location='takeAway')
    response = apiclient.get(url, data)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeshop.orders) == 0

def test_post_success(apiclient, coffeshop):
    url = '/order'
    data = dict(coffe='latte', size='large', milk='whole', location='takeAway')
    response = apiclient.post(url, data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.headers['Location'] == 'http://testserver/order/1'
    assert len(coffeshop.orders) == 1
    
    links = dict(
        self='http://testserver/order/1',
        update='http://testserver/order/1',
        cancel='http://testserver/order/1',
        payment='http://testserver/payment/1',
    )
    
    expected = dict(id = 1, coffe='latte', size='large', milk='whole', location='takeAway',
                    created_at=datetime(2021,4, 28), status='Placed', links=links)
    assert response.json() == expected

def test_post_badrequest(apiclient, coffeshop):
    url = '/order'
    data = dict(coffe='latte', size='large', milk='whole')
    response = apiclient.post(url, data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(coffeshop.orders) == 0    