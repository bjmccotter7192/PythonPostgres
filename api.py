import flask
import json
from flask import jsonify, request
from flask_cors import CORS

def create_app(test_config=None):
    app = flask.Flask(__name__)
    CORS(app)

    @app.route('/test', methods=['GET'])
    def testGet():
        return {
            "id": 1,
            "name": "Beej",
            "number": 123456789,
            "street_addr": "123 Something Street",
            "city": "SomeCity",
            "state": "State City",
            "zip": 11111 
        }, 200

    return app