from http import HTTPStatus
import pytest


def test_delete_success(apiclient, onecoffee):
    url = '/order/1'
    response = apiclient.delete(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(onecoffee.orders) == 1
    assert onecoffee.read(1).is_cancelled()

@pytest.mark.skip
def test_delete_badreq(apiclient, onecoffee):
    url = '/order'
    response = apiclient.delete(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(onecoffee.orders) == 1

@pytest.mark.skip
def test_delete_not_allowed(apiclient, onecoffee):
    url = '/order/1'
    response = apiclient.post(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(onecoffee.orders) == 1

def test_delete_not_found(apiclient, onecoffee):
    url = '/order/404'
    response = apiclient.delete(url)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert len(onecoffee.orders) == 1