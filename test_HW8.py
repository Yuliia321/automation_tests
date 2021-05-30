import requests

def test_create_role(role_payload,book , base_url):
    role_payload.update({"book"  : book["id"]})
    resp = requests.post(f"{base_url}/roles", data = role_payload)
    print(resp.text)
    assert resp.status_code == 201
    resp_body =  resp.json()

