from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import check_password_hash
from app import db
from app.models.user import User
from datetime import timedelta


auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/register", methods=["POST"])
@jwt_required()
def register():
    """
    Register user
    
    Return:
        Suscess or error message
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@auth_blueprint.route("/login", methods=["POST"])
def login():
    """
    Login user and generate
    
    Return:
        JWT Token
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(hours=2))
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"}), 401

