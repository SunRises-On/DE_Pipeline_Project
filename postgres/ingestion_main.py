import configparser
from 
from restaurant_menu import McDonald_menu, Wingstop_menu, Taco_bell_menu

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

def create_conn(database,host,password,port,user):
