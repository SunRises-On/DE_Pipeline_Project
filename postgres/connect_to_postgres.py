# widely used PostgreSQL connector library
import psycopg2
#pip install psycopg2

conn = psycopg2.connect(
    host="localhost",
    port='5432',
    database="DE",
    user="postgres", 
    password="password")

def create_conn(database,host,password,port,user):
    
    print("Create connection.")
    
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    return conn