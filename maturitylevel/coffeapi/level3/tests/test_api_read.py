
from datetime import datetime
from http import HTTPStatus

import pytest

from coffeapi.level3.framework import deserialize
from coffeapi.level3.domain import Status

def test_read_success(apiclient, onecoffee):
    url = '/order/1'
    response = apiclient.get(url)

    assert response.status_code == HTTPStatus.OK   

    links = dict(
        self='http://testserver/order/1',
        update='http://testserver/order/1',
        cancel='http://testserver/order/1',
        payment='http://testserver/payment/1',
    )

    expected = dict(id = 1, coffe='latte', size='large', milk='whole', location='takeAway', created_at=datetime(2021, 4, 28), status='Placed', links=links)
    assert response.json() == expected

def test_read_paid_links(apiclient, onecoffee):
    onecoffee.read(1).status = Status.Paid
    url = '/order/1'
    reponse = apiclient.get(url)

    links = dict(
        self='http://testserver/order/1',        
    )

    assert reponse.json()['links'] == links

def test_read_served_links(apiclient, onecoffee):
    onecoffee.read(1).status = Status.Served
    url = '/order/1'
    reponse = apiclient.get(url)

    links = dict(
        self='http://testserver/order/1',
        receipt='http://testserver/receipt/1',
    )

    assert reponse.json()['links'] == links

@pytest.mark.skip
def test_read_not_allowed(apiclient, onecoffee):
    url = '/order/1'
    response = apiclient.post(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

@pytest.mark.skip
def test_read_not_badrequest(apiclient, onecoffee):
    url = '/order'
    response = apiclient.get(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_read_not_found(apiclient, onecoffee):
    url = '/order/2'
    response = apiclient.get(url)

    assert response.status_code == HTTPStatus.NOT_FOUND

    
