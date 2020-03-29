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

        console.log("INSIDE GET GRAPH")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=months,
            y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
            name='Primary Product',
            marker_color='indianred'
        ))
        fig.add_trace(go.Bar(
            x=months,
            y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
            name='Secondary Product',
            marker_color='lightsalmon'
        ))
        # Here we modify the tickangle of the xaxis, resulting in rotated labels.
        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        # fig.show()
        pio.write_html(fig, file='./html/customer.html', auto_open=False)

    return app