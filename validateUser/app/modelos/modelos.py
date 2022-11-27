from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import relationship
import boto3


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password1 = db.Column(db.String(50))
    email = db.Column(db.String(100))