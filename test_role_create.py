import requests
import pytest

def test_create_role(book , base_url):
    role_data = {"name": "Unknown", "type": "Drama","level": 2 , "book"  : book["id"]}
    resp = requests.post(f"{base_url}/roles", data = role_data)
    assert resp.status_code == 201
    resp_body =  resp.json()



    resp_get = requests.get(f"{base_url}/roles/{resp_body['id']}")
    assert resp_get.status_code == 200
    resp_body  = resp_get.json()
    assert "id" in resp_body
    for key in role_data :
        assert resp_body[key] == role_data[key]

def test_update_role(role, book , base_url):
    role_data = {"level": 4 }
    respose = requests.put(f"{base_url}/roles/{role['id']}" , data = role_data)
    resp_body = respose.json()
    assert respose.status_code == 200
    for key in role_data:
        assert resp_body[key] == role_data[key]

payload_list = [
    {"level": 2147483648 },
    {"level": -2147483649 },
    {"level": "v" },
    {"type": 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 }
]
@pytest.mark.parametrize("role_data" , payload_list)

def test_update_role_level_out_of_range_max(role_data, role, book , base_url):
    # role_data = {"level": 2147483648 }
    respose = requests.put(f"{base_url}/roles/{role['id']}" , data = role_data)
    resp_body = respose.json()
    assert respose.status_code == 400
    print(resp_body)

# def test_update_role_level_out_of_range_min(role, book , base_url):
#     role_data = {"level": -2147483649 }
#     respose = requests.put(f"{base_url}/roles/{role['id']}" , data = role_data)
#     resp_body = respose.json()
#     assert respose.status_code == 400
#     print(resp_body)

# def test_update_role_level_incorrect_type(role, book , base_url):
#     role_data = {"level": "v" }
#     respose = requests.put(f"{base_url}/roles/{role['id']}" , data = role_data)
#     resp_body = respose.json()
#     assert respose.status_code == 400
#     print(resp_body)


payload_list = [
    { "type": "Drama","level": 2 },
    { "name": "Unknown", "type": "Drama","level": 2   }
]

@pytest.mark.parametrize("role_data",payload_list)

def test_create_role_without_name(role_data,book , base_url):
    # role_data = { "type": "Drama","level": 2 , "book"  : book["id"]}
    payload_list.append ({"book": book["id"]})
    resp = requests.post(f"{base_url}/roles", data = role_data)
    assert resp.status_code == 400
    print(resp.json())


def test_create_role_without_id(role_data, book , base_url):
    payload_list.append({  "book"  : book["id"]+1})
    resp = requests.post(f"{base_url}/roles", data = role_data)
    assert resp.status_code == 400
    print(resp.json())

# def test_update_role_type_out_of_range(role, book , base_url):
    # role_data = {"type": 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 }
    # respose = requests.put(f"{base_url}/roles/{role['id']}" , data = role_data)
    # resp_body = respose.json()
    # assert respose.status_code == 400
    # print(resp_body)


