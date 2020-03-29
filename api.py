import flask
import json
import db
from flask import jsonify, request
from flask_cors import CORS
import plotly.graph_objects as go
import plotly.io as pio

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

    @app.route('/getClients', methods=['GET'])
    def getClients():
        conn = db.connectToDb()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients;")
        query_results = cur.fetchall()

        rows = []
        for i in query_results:
            rows.append({
                "first_name": i[0],
                "last_name": i[1],
                "mi_initial": i[2],
                "number1": i[3],
                "number2": i[4],
                "email_address": i[5],
                "realtor": i[6],
                "referred_by": i[7]
            })

        print(rows)
        cur.close() 
        conn.close()

        return jsonify(rows)

    @app.route('/getGraph', methods=['GET'])
    def getGraph():

        print("INSIDE GET GRAPH")
        returnData = []
        
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for num, month in enumerate(months, start=1):
            returnData.append({
                "name": month,
                "value": num
            })

        return jsonify(returnData)

    return app