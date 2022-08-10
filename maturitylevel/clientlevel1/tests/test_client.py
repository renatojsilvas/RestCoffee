from http import HTTPStatus

from clientlevel1.client import create_order, delete_order, read_order, update_order
import httpretty

@httpretty.activate
def test_create():
    httpretty.register_uri(
        httpretty.POST,
        'http://127.0.0.1:8000/order/create?coffe=latte&size=large&milk=whole&location=takeAway',
        'coffe=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large',
        status=HTTPStatus.CREATED,
        match_querystring=True
    )

    assert create_order('latte', 'large', 'whole', 'takeAway') == 1

@httpretty.activate
def test_delete():
    httpretty.register_uri(
        httpretty.POST,
        'http://127.0.0.1:8000/order/delete?id=1',
        status=HTTPStatus.NO_CONTENT,
        match_querystring=True
    )

    assert delete_order(id=1)

@httpretty.activate
def test_read():
    httpretty.register_uri(
        httpretty.GET,
        'http://127.0.0.1:8000/order/read?id=1',
        'coffe=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large',
        status=HTTPStatus.OK,
        match_querystring=True
    )

    assert read_order(id=1) == {
        'coffe': 'latte',
        'id': '1',
        'location': 'takeAway',
        'milk': 'whole',
        'size': 'large'
    }

@httpretty.activate
def test_update():
    httpretty.register_uri(
        httpretty.POST,
        'http://127.0.0.1:8000/order/update?coffe=latte&id=1&size=large&milk=whole&location=dineIn',
        'coffe=latte\nid=1\nlocation=dineIn\nmilk=whole\nsize=large',
        status=HTTPStatus.NO_CONTENT,
        match_querystring=True
    )

    assert update_order(1, 'latte', 'large', 'whole', 'dineIn') == 1