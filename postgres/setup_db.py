

#check tables and schema, and print results
def print_tbl(cursor):

    print("Print tables in schema = 'public' ")

    query="""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'"""

    cursor.execute(query)

    #check if table is in database
    for table in cur.fetchall():
        print(table)

    return cursor