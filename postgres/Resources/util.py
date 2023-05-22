#Python imports
import datetime
#pip install psycopg2
import random
from Classes.item import Item
##################################################################################
# Summary: Function for getting a random number from a range.
#################################################################################
def get_rand_ran(tup):
    rnum = random.randrange(tup[0], tup[1])
    return rnum

##################################################################################
# Summary: Function for incrementing date.
#################################################################################

def increment_date(date_obj):
    date_obj += datetime.timedelta(days=1)
    return date_obj

##################################################################################
#  Explanation: Functions for column 3.
#  Summary: Determines the delivery_method, which is delivery or pickup.            
##################################################################################
def get_delivery_method(delivery_list, tup):
    rnum = get_rand_ran(tup)
    delivery_method = delivery_list[rnum]
    return delivery_method
##################################################################################
#  Explanation: Function for column 4.
#  Summary: Get a list of Object Item, representing items ordered.
#################################################################################
def get_csv_from_dict(items):
    new_list = []
    for x in items:
        name = x.name
        new_list.append(name)
    new_csv = '|'.join(new_list)
    return new_csv

def get_Item_Index(menu):
    index = random.randrange(0,len(menu))
    return index
def get_items(vendor_id, tup, vendor_dict):
    
    items = []
    items_ordered = get_rand_ran(tup)
    menu = vendor_dict[vendor_id] #get menu dictionary

    for x in range(items_ordered):
        index = get_Item_Index(menu)
        name = list(menu)[index] #key
        price = list(menu.values())[index] #value

        item = Item(name, price)
        items.append(item)
    
    return items

##################################################################################
#  Explanation: Function for column 6. 
#  Summary: Get tax rate for order.
#################################################################################
def get_tax(tax_list,tup):
    rnum = get_rand_ran(tup)
    tax = tax_list[rnum]
    return tax
##################################################################################
#  Explanation: Functions for column 9
#  Summary: Get random customer id by first finding a random index. Then    
#           getting the customer id from the customer_id_list.
#################################################################################
def get_customer_id(tup, customer_id_list):
    rnum = get_rand_ran(tup)
    customer_id = customer_id_list[rnum]
    return customer_id