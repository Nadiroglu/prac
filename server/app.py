from models import db, User, Event, Merch
from flask_migrate import Migrate
import stripe
from flask import Flask, request, make_response, jsonify, session, redirect, json
from flask_restful import Api, Resource
from flask_cors import CORS
import os
from datetime import datetime


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'asdcasdcasdacsd'
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# stripe.api_key = 'sk_test_51P5xgsKiofAVDtVIgVKnPOZh63ZLc2CyZvWeQGJloskP35dw7LOeasSFnkMVgQ7V9wzObP77q0oTDVRs7Gmpr7Ny00iXobH4bn'

api = Api(app)
CORS(app, supports_credentials=True)


@app.route('/')
def home():
    message = 'Welcome'
    return jsonify(message), 200


@app.route('/events')
def get_events():
    events = Event.query.all() 
    event_dict = []

    for event in events:
        event_dict.append(event.to_dict())

    return event_dict, 200


@app.route('/merchs')
def get_merchs():
    merchs = Merch.query.all()

    merch_dict = []

    for merch in merchs:
        merch_dict.append(merch.to_dict())

    return merch_dict, 200

if __name__ == "__main__":
    app.run(port=5555, debug=True)