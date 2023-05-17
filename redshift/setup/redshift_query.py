import redshift_connector
# for some reason result set is not working

def create_schema(conn, cursor, database, role):
    
    #cursor = drop_schema(conn, cursor)
    #conn = db_commit(conn)
    

    print("In create_schema")
    query= f"""create external schema if not exists myspectrum_schema 
    from data catalog
    database '{database}'
    iam_role '{role}'
    create external database if not exists;
    """

    cursor.execute(query)
    conn = db_commit(conn)

    cursor = print_external_schemas(cursor)
    

def drop_schema(conn, cursor):
    print("Dropping external schema ....")

    query = f"""drop schema if exists myspectrum_schema
    drop external database;"""

    try:
        cursor.execute(query)

    except Exception as e:
        print(e)

    return cursor

def print_external_schemas(cursor):

    print("Checking for external schemas...")

    query = "SELECT * FROM svv_external_schemas;"
    
    cursor.execute(query)

    try:
        result: tuple = cursor.fetchall()
        print(result)
    except Exception as e:
        print(e)

    return cursor

def db_commit(conn):

    try:
        conn.commit()
    except Exception as e:
        print(e)
    
    return conn