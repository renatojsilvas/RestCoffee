"""
- quem é o cliente
- os dados do pedido
- montar url
- Fazer um get
- imprimir o id do pedido
"""

import argparse
from email import parser
import json
import requests

BASE_URL = 'http://127.0.0.1:8000'

def post(coffee, size, milk, location):
    url = (f'{BASE_URL}/order')
    data = dict(coffe='latte', size='large', milk='whole', location='takeAway')
    headers = {'content-type': 'application/json'}   

    r = requests.post(url, data=json.dumps(data), headers=headers)    

    return r.headers['Location']

def get(url):    
    headers = {'content-type': 'application/json'}   
    r = requests.get(url, headers=headers)
    return r.json()

def build_parser(): 
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    sp_order = subparsers.add_parser('order')
    sp_order.add_argument('coffe')
    sp_order.add_argument('size')
    sp_order.add_argument('milk')
    sp_order.add_argument('location')

    return parser


if __name__ == '__main__':
    
    parser = build_parser()
    args = parser.parse_args()

    print(get(post(args.coffe, args.size, args.milk, args.location)))
