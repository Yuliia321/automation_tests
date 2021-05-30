import requests
import pytest


def test_get_filter(  base_url):
    r = requests.get(f'{base_url}/roles/?type=Senior Wizard')
    assert r.status_code == 200
    print(r.json())




def test_get_filter1( base_url):
    r = requests.get(f'{base_url}/roles/?level__lt=1')
    assert r.status_code == 200


def test_get_filter2( base_url):
    r = requests.get(f'{base_url}/roles/?level__lt=100')
    assert r.status_code == 200

def test_get_filter3( base_url):
    r = requests.get(f'{base_url}/roles/?level_lt=100')
    assert r.status_code == 500



def test_get_filter4( base_url):
    r = requests.get(f'{base_url}/roles/?book_id=1')
    assert r.status_code == 200

