import pytest

def test_create_task(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post('/api/tasks', json={"description": "Buy groceries"}, headers=headers)
    print(response)
    assert response.status_code == 201
    assert response.json["description"] == "Buy groceries"

def test_get_tasks(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get('/api/tasks', headers=headers)
    assert response.status_code == 200