"""
API Routes module.

Defines endpoints to manage tasks.
"""

from flask import Blueprint, request, jsonify

task_routes = Blueprint("tasks", __name__)


@task_routes.route("/tasks", methods=["GET"])
def list_tasks():
    """
    List all tasks.

    Returns:
        Response: Task list in JSON format.
    """
    from app.services.task_service import get_all_tasks

    tasks = get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])


@task_routes.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """
    Get task by ID.

    Args:
        task_id (int): Task id.

    Returns:
        Response: Task data or error message
    """
    from app.services.task_service import get_task_by_id

    task = get_task_by_id(task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({"error": "Task not found"}), 404


@task_routes.route("/tasks", methods=["POST"])
def add_task():
    """
    Add new task.

    Returns:
        Response: Task created or error message
    """
    from app.services.task_service import create_task

    data = request.get_json()
    if "description" not in data:
        return jsonify({"error": "Description is required"}), 400
    task = create_task(description=data["description"])
    return jsonify(task.to_dict()), 201


@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    """
    Edit task by id.

    Args:
        task_id (int): Task id.

    Returns:
        Response: Updated task data or error message
    """
    from app.services.task_service import update_task

    data = request.get_json()
    try:
        task = update_task(task_id, data.get("description"), data.get("status"))
        if task:
            return jsonify(task.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 401

    return jsonify({"error": "Task not found"}), 404


@task_routes.route("/tasks/status/<string:status>", methods=["GET"])
def list_tasks_by_status(status):
    """
    List tasks filtered by status.

    Args:
        status (str): Task status.

    Returns:
        Response: Task list in JSON format.
    """
    from app.services.task_service import get_tasks_by_status

    tasks = get_tasks_by_status(status)
    return jsonify([task.to_dict() for task in tasks])


@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    """
    Delete task by id.

    Args:
        task_id (int): Task id.

    Returns:
        Response: success or error message
    """
    from app.services.task_service import delete_task

    if delete_task(task_id):
        return jsonify({"message": "Task deleted successfully"})
    return jsonify({"error": "Task not found"}), 404
