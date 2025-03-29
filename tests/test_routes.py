import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_task(client):
    response = client.post('/api/tasks', json={"description": "Buy groceries"})
    assert response.status_code == 201
    assert response.json["description"] == "Buy groceries"

def test_get_tasks(client):
    response = client.get('/api/tasks')
    assert response.status_code == 200