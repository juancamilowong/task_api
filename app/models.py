"""
Task model.

Define task model and table.
"""

from datetime import datetime
from app import db


class Task(db.Model):
    """
    Represents task in a database.

    Atributos:
        id (int): Identifier.
        description (str): Task decription.
        status (str): Task status (TODO, IN_PROGRESS, DONE).
        created_at (datetime): Creation date.
        updated_at (datetime): Last update date.
    """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="TODO")
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def to_dict(self):
        """
        Transform Object to dict.

        Returns:
            dict: task dict.
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
