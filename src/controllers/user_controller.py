from flask import jsonify, request
from models.user_model import User
from Schemas.user_schema import UserSchema
from models.user_model import db

def create_user():
    user_schema = UserSchema()
    user_data = user_schema.load(request.json)
    user = User(**user_data)
    db.session.add(user)  # agrega el nuevo usuario a la sesión
    db.session.commit()  # guarda los cambios en la base de datos
    return user_schema.dump(user), 201

def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return user_schema.dump(users), 200

def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_schema = UserSchema()
    return user_schema.dump(user), 200

def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user_schema = UserSchema()
    user_data = user_schema.load(request.json, partial=True) # Carga los datos del request
    for key, value in user_data.items():
        setattr(user, key, value) # Actualiza el valor del atributo correspondiente en la instancia de User
    db.session.commit() # Guarda los cambios en la base de datos
    return user_schema.dump(user), 200

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user) # Elimina la instancia de User de la sesión de base de datos
    db.session.commit() # Guarda los cambios en la base de datos
    return '', 204