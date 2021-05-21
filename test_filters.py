import requests


def test_get_filter(role,  base_url):
    r = requests.get(f'{base_url}/roles/?type=Senior Wizard')
    assert r.status_code == 200


def test_get_filter( base_url):
    r = requests.get(f'{base_url}/roles/?level=1')
    assert r.status_code == 200
    print(r.json())

