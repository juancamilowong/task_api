"""
Create global fixtures used for all tests
"""
import pytest
from app import create_app, db
from app.models.user import User
from app.models.task import Task
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    """
    Config global test database 
    """
    app = create_app("testing")
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            db.session.add(User(username="admin", password=generate_password_hash("1234")))
            db.session.add(Task(description="TEST", status="TODO"))
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()

@pytest.fixture
def auth_token(client):
    """
    Get valid authentication token

    Returns:
        JWT token
    """
    response = client.post("/auth/login", json={"username": "admin", "password": "1234"})
    return response.get_json()["access_token"]
