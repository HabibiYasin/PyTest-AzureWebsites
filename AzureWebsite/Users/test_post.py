import requests
import json

def test_create_new_user_positive():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Users"
    headers = {
        "accept": "*/*",
        "Content-Type": "application/json; v=1.0"
    }
    payload = {
        "id": 0,
        "userName": "habibi77",
        "password": "valid123"
    }
    response = requests.post(url, headers=headers, json=payload)
    respJson = response.json()
    assert response.status_code == 200    
    assert respJson.get('id') == payload.get('id')
    assert respJson.get('userName') == payload.get('userName')
    assert respJson.get('password') == payload.get('password')

def test_successful_registration():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Users"
    data = {
        "id": 0,
        "userName": "habibi77",
        "password": "valid123"
    }
    response = requests.post(url, json=data)
    responseJson = response.json()
    assert response.status_code == 200
    assert 'id' in responseJson
    assert 'userName' in responseJson
    assert 'password' in responseJson