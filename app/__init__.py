"""
Flask initialization module.

Create Flask application, set database and register blueprints.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()


def create_app():
    """
    Create and configure Flask application.

    Returns:
        Flask: Flask application configured.
    """
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate = Migrate(app, db)

    from app.routes.task_routes import task_routes

    app.register_blueprint(task_routes, url_prefix="/api")

    return app
