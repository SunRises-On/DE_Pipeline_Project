#connect to the cluster

#pip install redshift_connector
import redshift_connector

def create_conn(host,database, user, password):
    print("create a connection")
    conn = redshift_connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    return conn


def create_cursor(conn):
    
    #print("enable autoconnect")
    #conn.autocommit = True

    print("create cursor")
    cursor: redshift_connector.Cursor = conn.cursor()
    print("cursor created")

    return cursor