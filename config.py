import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'task-manager-secret-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True 