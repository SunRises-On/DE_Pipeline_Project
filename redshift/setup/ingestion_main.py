import os
import configparser
from get_confi import get_file_path
from connect_to_redshift import create_conn,create_cursor
from redshift_query import setup_rdshft

print('Get config file from host computer')
# r'config.ini'
#get the absolute path

fn = 'config.ini'
file_path = get_file_path(fn)
print(f"file path = {file_path}")

print('Read config file')
config = configparser.ConfigParser()

configFilePath = str(file_path)
print(f"{configFilePath}")
config.read(configFilePath)

print('Fetch parameters')
user=config.get('aws','username')
password=config.get('aws','password')
host=config.get('aws','host')
database=config.get('aws','database')

role=config.get('redshift','role')
redshift_db=config.get('redshift','database')
user_tbl=config.get('redshift','user_tbl')
schema=config.get('redshift','schema')

bucket=config.get('s3','bucket')

print('Connecting to Redshift instance')

exit()

print('Create a cursor object')
print(f"database = {database}")

conn = create_conn(host,database, port, user, password)
cursor = create_cursor(conn)

print('Create schema if not exists.')
setup_rdshft(bucket,conn, cursor, redshift_db, role, schema, user_tbl)
#print('Query a table')