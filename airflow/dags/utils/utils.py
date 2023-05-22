import os
#Psycopg is a PostgreSQL adapter for the Python programming language. 
# It is a wrapper for the libpq, the official PostgreSQL client library.
#install from terminal
# pip install psycopg2-binary
import psycopg2



# in your create s3 bucket terminal
# pip install 'apache-airflow[amazon]'


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
