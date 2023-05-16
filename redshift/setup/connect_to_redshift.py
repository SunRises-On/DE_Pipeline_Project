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

    cursor = conn.cursor()

    return cursor