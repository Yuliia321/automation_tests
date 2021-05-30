import requests
import pytest

""" Параметризация Create теста данными из файла """

def test_create_role(role_payload,book , base_url):
    role_payload.update({"book"  : book["id"]})
    resp = requests.post(f"{base_url}/roles", data = role_payload)
    print(resp.text)
    assert resp.status_code == 201
    resp_body =  resp.json()

"""параметризация Read теста с фильтрами"""

payload_list = [
    {"level" : 1},
    {"level" : 10}
]

@pytest.mark.parametrize("payload_list" , payload_list)

def test_get_filter1( payload_list, base_url):
    r = requests.get(f'{base_url}/roles/', params = payload_list)
    print(r.json())
    assert r.status_code == 200

