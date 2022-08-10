import httpretty
from clientlevel0.core import place_order

@httpretty.activate
def test_placeorder():
    httpretty.register_uri(
        httpretty.GET,
        'http://127.0.0.1:8000/PlaceOrder?coffe=latte&size=whole&milk=large&location=takeAway',        
        'Order=1',
        match_querystring=True
    )
    assert place_order('latte', 'whole', 'large', 'takeAway') == '1'