import psycopg2
import os

def connectToDb():
    conn = psycopg2.connect(host=os.environ['DB_HOST'], port = 5432, 
                            database=os.environ['DB_DB'], 
                            user=os.environ['DB_USER'], 
                            password=os.environ['DB_PASSWORD'])
    return conn
