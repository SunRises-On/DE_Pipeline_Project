# widely used PostgreSQL connector library
import psycopg2
#pip install psycopg2



def create_conn(database,host,password,port,user):
    
    print("Create connection.")

    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    #set auto commit 
    conn.autocommit = True

    return conn

def create_cursor(conn):
    #create a cursor object
    print("Create cursor.")

    cursor = conn.cursor()
    
    return cursor