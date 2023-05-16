import os
import configparser
from get_confi import get_file_path
from connect_to_redshift import create_cursor


print('Get config file')
# r'config.ini'
#get the absolute path

fn = 'config.ini'
file_path = get_file_path(fn)
print(f"file path = {file_path}")

exit()
print('Read config file')
config = configparser.ConfigParser()

config.read(file_path)

print('Fetch parameters')
user=config.get('aws','username')
password=config.get('aws','password')
host=config.get('aws','host')
port=config.get('aws','port')
database=config.get('aws','database')

print('Connecting to Redshift instance')

print('Create a cursor object')
cursor = create_cursor(host,database,port,user,password
)

#print('Query a table')