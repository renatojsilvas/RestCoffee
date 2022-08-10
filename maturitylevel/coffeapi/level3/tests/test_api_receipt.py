from http import HTTPStatus
import pytest

from coffeapi.level3.domain import Status


def test_receipt_success(apiclient, onecoffee):
    url = '/receipt/1'
    response = apiclient.delete(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(onecoffee.orders) == 1
    assert onecoffee.read(1).is_collected()

@pytest.mark.skip
def test_receipt_badreq(apiclient, onecoffee):
    url = '/order'
    response = apiclient.delete(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(onecoffee.orders) == 1

@pytest.mark.skip
def test_receipt_not_allowed(apiclient, onecoffee):
    url = '/order/1'
    response = apiclient.post(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(onecoffee.orders) == 1

def test_receipt_not_found(apiclient, onecoffee):
    url = '/receipt/404'
    response = apiclient.delete(url)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert len(onecoffee.orders) == 1

def test_receipt_already_delivered(apiclient, onecoffee):
    onecoffee.read(1).status = Status.Collected
    
    url = '/receipt/1'   

    response = apiclient.delete(url, data={})

    assert response.status_code == HTTPStatus.CONFLICT 