from asyncore import read
from http import HTTPStatus
from urllib import response


def test_update_sucess(client, onecoffee):
    url = '/order/update?id=1&coffe=curto&milk=&size=small&location=takeAway'
    response = client.post(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(onecoffee.orders) == 1
    assert (dict(coffe='curto', milk='', size='small', id=1, location='takeAway')
           == vars(onecoffee.read(1)))

def test_update_not_allowed(client):
    url = '/order/update?id=1&coffe=curto&milk=&size=small&location=takeAway'
    response = client.get(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED    

def test_update_not_allowed(client):
    url = '/order/update'
    response = client.post(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST 

def test_update_not_allowed(client):
    url = '/order/update?id=4&coffe=curto&milk=&size=small&location=takeAway'
    response = client.post(url)

    assert response.status_code == HTTPStatus.NOT_FOUND 