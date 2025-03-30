"""
Flask initialization module.

Create Flask application, set database and register blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import DefaultConfig, TestingConfig

db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_name="default"):
    """
    Create and configure Flask application.

    Returns:
        Flask: Flask application configured.
    """
    app = Flask(__name__)
    CORS(app)
    if config_name == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DefaultConfig)

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.task import task_routes
    from app.routes.auth import auth_blueprint

    app.register_blueprint(task_routes, url_prefix="/api")
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
