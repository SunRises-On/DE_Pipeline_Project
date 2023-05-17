import redshift_connector
# for some reason result set is not working



def setup_rdshft(bucket, conn, cursor, database, role, schema, user_tbl):

    #cursor = drop_schema(cursor)
    #conn = db_commit(conn)
    

    cursor = create_schema(cursor, database, role, schema)
    conn = db_commit(conn)

    #check if schema was created log later
    cursor = print_external_schemas(cursor)

    #drop tbl if exists

    #create table
    #set autocommit to true to allow create external table
    #make sure we're not in a transaction
    conn.rollback()
    conn.autocommit = True
    cursor = create_tbl(bucket, cursor, schema, user_tbl)
    conn.autocommit = False

    #print all tables ....

    print("close cursor.")
    cursor.close()
    
def create_schema(cursor, database, role, schema):

    print("In create_schema")

    query= f"""create external schema 
    if not exists {schema} 
    from data catalog
    database '{database}'
    iam_role '{role}'
    create external database if not exists;
    """
    try:
        cursor.execute(query)
    
    except Exception as e:
        print(e)

    return cursor

def drop_schema(cursor, schema):
    print("Dropping external schema ....")

    query = f"""drop schema if exists {schema}
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

def create_tbl(bucket, cursor, schema, user_tbl):

    print("In create_tbl.")
    # schema_name = myspectrum_schema
    query = f"""CREATE EXTERNAL TABLE
        {schema}.{user_tbl}(
            invoice_number INTEGER, 
            vendor_id INTEGER,
            delivery_method VARCHAR(8),
            menu_items VARCHAR(200),
            invoice_date DATE,
            tax NUMERIC(5,5),
            total NUMERIC,
            customer_id INTEGER
        ) PARTITIONED BY (insert_date DATE)
          ROW FORMAT DELIMITED FIELDS
          TERMINATED BY ',' 
          STORED AS TEXTFILE 
          LOCATION
          's3://{bucket}/stage/user_purchase/'
          TABLE PROPERTIES
          ('skip.header.line.count'='1');   
    """
    try:
        cursor.execute(query)
    
    except Exception as e:
        print(e)

    return cursor