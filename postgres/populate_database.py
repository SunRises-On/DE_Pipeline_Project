

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

cursor = get_last_row(cursor)


def get_tbl_count(cursor):
    query = """SELECT COUNT(*) FROM user_purchase """

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print(e)
    
    return cursor

cursor = get_tbl_count(cursor)



