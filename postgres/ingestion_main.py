import configparser
from connect_to_postgres import create_conn, create_cursor
from setup_db import print_tbl, delete_tbl_data
from pop_db import populate

print("Read config file.")
fn = 'config.ini'

config = configparser.ConfigParser()
config.read(fn)

print('Fetch parameters')

host=config.get('postgres','host')
port=config.get('postgres','port')
database=config.get('postgres','database')
user=config.get('postgres','user')
password=config.get('postgres','password')

print('Connect to database.')

conn = create_conn(database,host,password,port,user)
cursor = create_cursor(conn)

print('Select all tables in schema public')
cursor = print_tbl(cursor)

print('Delete all data from table')
cursor = delete_tbl_data(cursor)

print('Populate table.')
cursor = populate(cursor)



print('Close the connection.')
conn.close()
