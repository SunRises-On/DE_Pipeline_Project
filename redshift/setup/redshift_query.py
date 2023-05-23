import redshift_connector
# for some reason result set is not working



def setup_rdshft(bucket, conn, cursor, database, role, schema, user_tbl):

    cursor = drop_schema(cursor, schema)
    conn = db_commit(conn)
    
    cursor = create_schema(cursor, database, role, schema)
    conn = db_commit(conn)

    #check if schema was created log later
    cursor = print_external_schemas(cursor)

    #drop tbl if exists
    conn.rollback() #make sure we aren't in a transaction
    conn.autocommit = True #turn autocommit on as drop & create cannot be in transaction block
    cursor = drop_tbl(cursor, schema, user_tbl)
   # conn.autocommit = False

    #create table
    cursor = create_tbl(bucket, cursor, schema, user_tbl)
    conn.autocommit = False

    #print all tables ....
    cursor = print_external_tbl(cursor,schema)

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
    
    try:
        cursor.execute(query)
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

def drop_tbl(cursor, schema, user_tbl):

    print("In drop_tbl")

    query = f"DROP TABLE IF EXISTS {schema}.{user_tbl}"

    try:
        cursor.execute(query)
    
    except Exception as e:
        print(e)

    return cursor

# Code - PARTITIONED BY (insert_date DATE)
# Explanation -  partitions it by DATE with column name = insert_date
# Doc - [ PARTITIONED BY (col_name data_type [, … ] )]

# Code - TABLE PROPERTIES ('skip.header.line.count'='1')
# Explanation - Most datasets (CSV files, Text files, etc)
#               Have header rows inside the data, and loading them into Hive
#               tables will result with null values. The 'skip.header.line.count' will
#               prevent that.
# Doc - [ TABLE PROPERTIES ( 'property_name'='property_value' [, ...] ) ]

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
          ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
          STORED AS TEXTFILE 
          LOCATION 's3://{bucket}/stage/user_purchase/'
          TABLE PROPERTIES ('skip.header.line.count'='1');   
    """
    try:
        cursor.execute(query)
    
    except Exception as e:
        print(e)

    return cursor

def print_external_tbl(cursor,schema):

    print("Checking for external tables...")

#select schemaname, tablename from svv_external_tables where schemaname = 'apg_tpch';
    query = f"""SELECT schemaname, tablename 
                FROM svv_external_tables
                WHERE schemaname = '{schema}';"""

    
    cursor.execute(query)

    try:
        result: tuple = cursor.fetchall()
        print(result)
    except Exception as e:
        print(e)

    return cursor