import psycopg2
import os
import json

def connectToDb():
    if os.environ.get('DB_HOST'):
        conn = psycopg2.connect(host=os.environ['DB_HOST'], port = 5432, 
                                database=os.environ['DB_DB'], 
                                user=os.environ['DB_USER'], 
                                password=os.environ['DB_PASSWORD'])
    else:
        with open("config.json") as c:
            config = json.load(c)

        conn = psycopg2.connect(host=config.config['DB_HOST'], port = 5432, 
                                database=config.config['DB_DB'], 
                                user=config.config['DB_USER'], 
                                password=config.config['DB_PASSWORD'])
    return conn
