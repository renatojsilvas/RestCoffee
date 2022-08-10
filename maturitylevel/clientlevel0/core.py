import re
import requests

BASE_URL = 'http://127.0.0.1:8000'


def place_order(coffee, size, milk, location):
    url = f'{BASE_URL}/PlaceOrder?coffe={coffee}&size={size}&milk={milk}&location={location}'

    r = requests.get(url)
    order_id = ''.join(re.findall(r'Order=(\d+)', r.text))

    return order_id