import flask
import json
from flask import jsonify, request
from flask_cors import CORS

def create_app(test_config=None):
    app = flask.Flask(__name__)
    CORS(app)

    @app.route('/test', methods=['GET'])
    def testGet():
        return "OK", 200

    return app