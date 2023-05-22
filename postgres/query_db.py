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

#check tables and schema, and print results
def print_tbl(cursor):

    print("Print tables in schema = 'public' ")

    query="""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'"""

    try:
        cursor.execute(query)
        for table in cursor.fetchall():
            print(table)
            
    except Exception as e:
        print(e)

    return cursor


def delete_tbl_data(cursor):

    print("Delete old data from table.")
    #delete old table
    query = """DELETE FROM user_purchase;
    """
    try:
        cursor.execute(query)
    except Exception as e:
         print(e)


    return cursor

def get_last_row(cursor):
    #get last row of user_purchase
    query = """SELECT * FROM user_purchase
    WHERE invoice_number=(SELECT max(invoice_number) FROM user_purchase);
    """

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        print(result[0])
    except Exception as e:
        print(e)

    return cursor



def get_tbl_count(cursor):
    query = """SELECT COUNT(*) FROM user_purchase """

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print(e)
    
    return cursor