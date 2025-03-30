"""
User model.

Define user model and table.
"""

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    Represents user in a database.

    Attributes:
        id (int): Identifier.
        username (str): user name.
        password (str): Password.
        created_at (datetime): Creation date.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def set_password(self, password):
        """Stores the password in hashed format"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check if the password is correct"""
        return check_password_hash(self.password, password)