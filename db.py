import psycopg2
import os
import json

def connectToDb():
    # conn = psycopg2.connect(host=os.environ['DB_HOST'], port = 5432, 
    #                         database=os.environ['DB_DB'], 
    #                         user=os.environ['DB_USER'], 
    #                         password=os.environ['DB_PASSWORD'])

    conn = psycopg2.connect(host="localhost", port = 5432, 
                            database="test", 
                            user="postgres", 
                            password="postgres")
    return conn
