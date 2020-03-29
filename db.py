import psycopg2

def connectToDb():
    conn = psycopg2.connect(host="192.168.1.133", port = 5432, database="test", user="postgres", password="postgres")
    return conn
