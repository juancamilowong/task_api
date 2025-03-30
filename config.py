import os

class DefaultConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'task-manager-secret-key')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3307/tasksDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True 
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "a84ace1e66212d083cff98f18373569722e85a79")

class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "test-secret-key")