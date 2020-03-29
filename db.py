import psycopg2

def connectToDb():
    conn = psycopg2.connect(host="localhost", port = 5432, database="test", user="postgres", password="postgres")
    return conn
