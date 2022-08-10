from http import HTTPStatus
from coffeapi.level3.domain import Status

def test_payment_sucess(apiclient, onecoffee):
    url = '/payment/1'
    data = dict(amount=199)
    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.OK

    links = dict(
        self='http://testserver/order/1'
    )
    expected = dict(links=links)        
    assert response.json() == expected
    assert len(onecoffee.orders) == 1
    assert onecoffee.read(1).is_paid()

def test_payment_bad_request(apiclient, onecoffee):
    url = '/payment/1'
    data = dict()
    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST 
    assert len(onecoffee.orders) == 1
    assert not onecoffee.read(1).is_paid()

def test_payment_not_found(apiclient, onecoffee):
    url = '/payment/404'
    data = dict(amount='199')
    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.NOT_FOUND 

def test_payment_already_paid(apiclient, onecoffee):
    onecoffee.read(1).status = Status.Paid
    
    url = '/payment/1'
    data = dict(amount='199')    

    response = apiclient.put(url, data=data)

    assert response.status_code == HTTPStatus.CONFLICT 