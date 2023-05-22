# widely used PostgreSQL connector library
import psycopg2
#pip install psycopg2



def connect(database,host,password,port,user):
    
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

    print("Create cursor.")

    cursor = conn.cursor()

    return conn, cursor
