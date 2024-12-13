from models import db, User, Event, Merch
from flask_migrate import Migrate
import stripe
from flask import Flask, request, make_response, jsonify, session, redirect, json
from flask_restful import Api, Resource
from flask_cors import CORS
import os
from datetime import datetime
# from ddtrace import patch_all
# import logging
# from datadog import statsd




# Set Datadog environment variables
os.environ["DD_SERVICE"] = "flask-app"
os.environ["DD_ENV"] = "production"
os.environ["DD_LOGS_INJECTION"] = "true"


# patch_all()
# Initialize the Flask application
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'asdcasdcasdacsd'
app.json.compact = False


# Set up logging
# logger = logging.getLogger('myapp')
# logger.setLevel(logging.DEBUG)

# Custom logging format to include trace and span IDs
# formatter = logging.Formatter('%(asctime)s - %(message)s - Trace ID: %(trace_id)s - Span ID: %(span_id)s')
# ch = logging.StreamHandler()
# ch.setFormatter(formatter)
# logger.addHandler(ch)


# Initialize Migrate and database
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
CORS(app, supports_credentials=True)


# @app.route('/')
# def hello():
#     # Send a custom metric to Datadog
#     statsd.increment('flask.requests')
#     return "Hello, World!"

@app.route('/api/events')
def get_events():

    # app.logger.info("Fetching events from the database")
    events = Event.query.all()
    event_dict = [event.to_dict() for event in events]  # List comprehension for clarity

    # Increment a custom metric in Datadog

    return jsonify(event_dict), 200

@app.route('/merchs')
def get_merchs():
    merchs = Merch.query.all()
    merch_dict = [merch.to_dict() for merch in merchs]  # List comprehension for clarity
    return jsonify(merch_dict), 200

if __name__ == "__main__":
    app.run(port=5555, debug=True)
