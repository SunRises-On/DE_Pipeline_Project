#connect to the cluster

#pip install redshift_connector
import redshift_connector




def create_cursor(host,database,port,user,password):
    conn = redshift_connector.connect(
        host=host,
        database=database,
        port=port,
        user=user,
        password=password
    )
    print("create cursor")
    cursor = conn.cursor()
    print("cursor created")

    print("enable autoconnect")
    conn.autocommit = True
    return cursor