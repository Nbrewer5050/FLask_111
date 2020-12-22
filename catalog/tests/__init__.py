import requests
from pprint import pprint

def test_scan():
    resp = requests.get("http://127.0.0.1:5000/products")
    pprint(resp.json())

def test_read():
    resp = requests.get("http://127.0.0.1:5000/products"/1)
    pprint(resp.json())

def test_create():
    rsample = {"name": "laptop", "price": 1000.0, "description": "black"}
    resp = requests.post("http://127.0.0.1:5000/products/2", json=sample)
    pprint(resp.json())

def test_update():
    sample + {"name": "banana", "price": 1.0, "description": "Yellow"}
    resp = request.post("http://127.0.0.1:5000/products/8", json=sample)
    pprint(resp.json())

if __name__== "__main__":
    test_scan()
    test_read()
    test_create()
    test_update()