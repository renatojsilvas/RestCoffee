
from datetime import datetime
from http import HTTPStatus

import pytest

from coffeapi.level2.framework import deserialize

def test_read_success(apiclient, onecoffee):
    url = '/order_old/1'
    response = apiclient.get(url)

    assert response.status_code == HTTPStatus.OK    
    expected = dict(id = 1, coffe='latte', size='large', milk='whole', location='takeAway', created_at=datetime(2021, 4, 28), status='Placed')
    assert response.json() == expected

@pytest.mark.skip
def test_read_not_allowed(apiclient, onecoffee):
    url = '/order_old/1'
    response = apiclient.post(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

@pytest.mark.skip
def test_read_not_badrequest(apiclient, onecoffee):
    url = '/order_old'
    response = apiclient.get(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_read_not_found(apiclient, onecoffee):
    url = '/order_old/2'
    response = apiclient.get(url)

    assert response.status_code == HTTPStatus.NOT_FOUND

    
