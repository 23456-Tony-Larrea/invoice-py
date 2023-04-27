from flask import jsonify, request
from models.user_model import User
from Schemas.user_schema import UserSchema
from models.user_model import db
from flask_bcrypt import generate_password_hash,check_password_hash
import jwt
from datetime import datetime, timedelta

def register():
    user_schema = UserSchema()
    user_dict = user_schema.load(request.json)
    password = request.json.get('password_hash')
    password_hash = generate_password_hash(password.encode('utf-8'))
    user_dict['password_hash'] = password_hash
    user = User(**user_dict)
    db.session.add(user)
    db.session.commit()

    # Create JWT token with user name and email
    token_payload = {
        'name': user.name,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(days=7) # token expires in 7 days
    }
    token = jwt.encode(token_payload, 'my-secret-key', algorithm='HS256')

    # Add token to user model
    user.token = token
    db.session.commit()

    # Return response with user data and token
    response_data = {
        'user': user_schema.dump(user)
    }
    return jsonify(response_data), 201

def login():
    email=request.json.get('email')
    password=request.json.get('password')
    user=User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({'message':'User not found'}),404
    if not check_password_hash(password,user.password_hash):
                return jsonify({'message': 'Incorrect password'}), 401
    db.session.commit()

    # Return response with user data and token
    user_schema = UserSchema()
    response_data = {
        'user': user_schema.dump(user)
    }
    return jsonify(response_data), 200