from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import re
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()



class User(db.Model, SerializerMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password_hash = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    profile_picture_url = db.Column(db.String(255))
    role = db.Column(db.String, default = 'User')



class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    location = db.Column(db.String(100), nullable = False)
    date_time = db.Column(db.DateTime)
    category = db.Column(db.String)
    image_url = db.Column(db.String)

    merchs = db.relationship('Merch', back_populates = 'event')


class Merch(db.Model, SerializerMixin):
    __tablename__ = 'merchs'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    image_url = db.Column(db.String, nullable = False)

    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable = False)

    event = db.relationship('Event', back_populates = 'merchs')

    serialize_rules = ['-event']

