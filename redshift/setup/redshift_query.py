import redshift_connector


def create_schema(cursor, database, role):
    print("In create_schema")
    query= f"""create external if not exists schema myspectrum_schema
    from data catalog
    database '{database}'
    iam_role '{role}'
    create external database if not exists;
    """

    cursor.execute(query)

    result= cursor.fetchall()
    print(result)