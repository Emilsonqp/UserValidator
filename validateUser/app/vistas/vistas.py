from flask_restful import Resource
from ..modelos import db, User
from flask import request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import bcrypt
from sqlalchemy.sql import exists

class VistaSignIn(Resource):

    def post(self):
        password1 = request.json["password1"]
        password2 = request.json["password2"]
        email = request.json["email"]
        if password1 != password2:
            return {"message": "Passwords must match in order to Sign-In"}, 403

        password1 = bcrypt.hashpw((password1).encode('utf-8'), bcrypt.gensalt())
        exist_email = User.query.filter_by(email=email).first() is not None
        if exist_email:
            return {"message": "This Email match an existent account.Try again!"}, 403
        new_user = User(username=request.json["username"], password1=password1, email=email)
        access_token = create_access_token(identity=request.json["username"])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "user created successfully", "access_token": access_token}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204


class VistaLogIn(Resource):
    def get(self):
        return "pong"

    def post(self):
        u_username = request.json["username"]
        u_password1 = request.json["password1"]
        user = User.query.filter_by(username=u_username).first()
        db.session.commit()

        if user is None:
            return "The username do not exist", 404

        if not bcrypt.checkpw(u_password1.encode('utf8'), user.password1):
            return "Incorrect password"

        else:
            access_token = create_access_token(identity=user.username)
            return {"message": "Access granted", "username": {"username": user.username, "id": user.id},
                    "access_token": access_token}


class VistaValidaAgenda(Resource):
    @jwt_required()
    def get(self):
        return "Consulta de agenda exitosa"

class VistaCrearConsulta(Resource):
    @jwt_required()
    def post(self, id_consulta):
        return "Consulta creada con éxito"