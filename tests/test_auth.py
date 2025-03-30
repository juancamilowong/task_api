import json
from flask_jwt_extended import create_access_token

def test_login_success(client):
    response = client.post("/auth/login", json={"username": "admin", "password": "1234"})
    data = response.get_json()

    assert response.status_code == 200
    assert "access_token" in data

def test_login_failure(client):
    response = client.post("/auth/login", json={"username": "admin", "password": "wrong"})
    assert response.status_code == 401


def test_register_unauthorized(client):
    response = client.post("/auth/register", json={"username": "admin", "password": "1234"})
    assert response.status_code == 401  

def test_register(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/auth/register", json={"username": "new", "password": "4321"}, headers=headers)
    assert response.status_code == 201