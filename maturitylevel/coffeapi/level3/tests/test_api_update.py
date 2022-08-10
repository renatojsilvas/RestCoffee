from datetime import datetime
from http import HTTPStatus

import pytest

from coffeapi.level3.domain import Status

def test_update_sucess(apiclient, onecoffee):
    url = '/order/1'
    data = dict(coffe='curto', milk='', size='small', location='takeAway')
    response = apiclient.put(url, data=data)

    links = dict(
        self='http://testserver/order/1',
        update='http://testserver/order/1',
        cancel='http://testserver/order/1',
        payment='http://testserver/payment/1',
    )
    expected = dict(coffe='curto', milk='', size='small', id=1, location='takeAway',
                    created_at=datetime(2021, 4, 28), status='Placed', links=links)

    assert response.status_code == HTTPStatus.OK
    assert len(onecoffee.orders) == 1
    assert response.json() == expected

@pytest.mark.skip
def test_update_not_allowed(apiclient):
    url = '/order?id=1&coffe=curto&milk=&size=small&location=takeAway'
    response = apiclient.put(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED    

def test_update_bad_request(apiclient):
    url = '/order/1'
    data = dict(coffe='curto', milk='', size='small')
    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST 

def test_update_not_found(apiclient):
    url = '/order/404'
    data = dict(coffe='curto', milk='', size='small', location='takeAway')
    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.NOT_FOUND 