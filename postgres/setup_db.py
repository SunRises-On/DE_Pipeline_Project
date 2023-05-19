

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