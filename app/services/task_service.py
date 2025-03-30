"""
Task management persistence.

Define all the task management persistence.
"""

from datetime import datetime
from app import db
from app.models.task import Task

VALID_STATUS = ["TODO", "IN-PROGRESS", "DONE"]


def get_all_tasks():
    """Get all tasks"""
    return Task.query.all()


def get_task_by_id(task_id):
    """Get task by ID"""
    return Task.query.get(task_id)


def get_tasks_by_status(status: str):
    """Get tasks filtered by status"""
    return Task.query.filter_by(status=status).all()


def create_task(description, status="TODO"):
    """Create new task"""
    new_task = Task(description=description, status=status)
    db.session.add(new_task)
    db.session.commit()
    return new_task


def update_task(task_id, description=None, status=None):
    """Update task by ID"""
    task = Task.query.get(task_id)
    if not task:
        return None
    if description:
        task.description = description
    if status:
        if not status in VALID_STATUS:
            raise Exception("Status not valid")
        task.status = status

    task.updated_at = datetime.now()
    db.session.commit()
    return task


def delete_task(task_id):
    """Delete task by ID"""
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False
