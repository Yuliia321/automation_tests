import pytest
import requests
import json


@pytest.fixture()
def base_url():
    return "http://pulse-rest-testing.herokuapp.com"


@pytest.fixture()
def book(base_url):
    book_data = {"title" : "New", "author" :"new"}
    resp = requests.post(f"{base_url}/books", data = book_data)
    book = resp.json()
    yield book
    resp = requests.delete(f"{base_url}/books/{book['id']}")


@pytest.fixture()
def role(book, base_url):
    role_data = {"name": "Unknown", "type": "Drama", "level": 2, "book": book["id"]}
    resp = requests.post(f"{base_url}/roles", data=role_data)
    role = resp.json()
    yield role
    resp = requests.delete(f"{base_url}/roles/{role['id']}")



with open('data_test.json') as f:
        x = f.read()
        role_payload_list = json.loads(x)

@pytest.fixture(params=role_payload_list)
def role_payload(request):
    return request.param

