import os
#Psycopg is a PostgreSQL adapter for the Python programming language. 
# It is a wrapper for the libpq, the official PostgreSQL client library.
#install from terminal
# pip install psycopg2-binary
import psycopg2

# in your create s3 bucket terminal
# pip install 'apache-airflow[amazon]'

from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.S3_hook import S3Hook

def _local_to_s3(
    bucket_name: str, key: str, file_name: str, remove_local: bool = False
) -> None:
    #import s3 connection
    s3 = S3Hook('S3_conn')
    s3.load_file(
        filename=file_name, bucket_name=bucket_name, replace=True, key=key
    )
    if remove_local:
        if os.path.isfile(file_name):
            os.remove(file_name)

def run_redshift_external_query(qry: str) -> None:
    # postgres_conn_id – The postgres conn id reference to a specific postgres database.
    rs_hook = PostgresHook(postgres_conn_id="redshift_default")
    
    #Establishes a connection to a postgres database
    rs_conn = rs_hook.get_conn() 
    
    # No transaction is started when commands are executed and no commit() or rollback()
    # is required. Some PostgreSQL commands such as CREATE DATABASE can't run
    rs_conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    
    rs_cursor = rs_conn.cursor()
    rs_cursor.execute(qry)
    rs_cursor.close()
    rs_conn.commit()
    
    
