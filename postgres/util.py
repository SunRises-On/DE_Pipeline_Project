#Python imports
import datetime
#pip install psycopg2
import random
from decimal import Decimal

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
def get_col_3(delivery_list, tup):
    rnum = get_rand_ran(tup)
    delivery_method = delivery_list[rnum]
    return delivery_method
##################################################################################
#  Explanation: Function for column 4.
#  Summary: Get a dictionary of items ordered and their prices.
#################################################################################
def get_csv_from_dict(dictionary):
    new_list = list(dictionary)
    new_csv = '|'.join(new_list)
    return new_csv

def checkKey(item_dict, key):
    #check if empty
    #empty dictionary are false 
    if (bool(item_dict) == False):
        return False
    elif key in item_dict.keys():
        return True
    else:
        return False

def addItem(item_dict, menu):

    rnum = random.randrange(0,len(menu))
    key = list(menu)[rnum]
    val = list(menu.values())[rnum]
    #check if key already in item_dict
    isDuplicate = checkKey(item_dict, key)
    
   # try:
        #if duplicate  
    if(isDuplicate):
        x = item_dict[key]
        
        #check if x is zero
        #if it's zero do nothing
        #add a way to count zero items later
        if(x!=0):
        
            #check number of duplicates
            count = val/x
            #round to nearest integer 
            count = round(count)
            
            #example new burger is now
            # (1) Double Burger
            key = f"({count}) {key}"
            item_dict[key] = val
    #not duplicate add new key-value pair
    else:

        item_dict[key]=val

    #except (Exception) as error:
    #    print(error)
        
    
    return item_dict

#recursion continually add one more item until
# rnum = 0
def getItemList(menu, rnum, item_dict ):

    item_dict = item_dict
    if(rnum > 0):
        item_dict = addItem(item_dict, menu)
        getItemList(menu, rnum-1, item_dict)
    return item_dict

def get_item_dict(vendor_id, tup, vendor_dict):
    
    items_ordered = get_rand_ran(tup)

    menu_dict = vendor_dict[vendor_id] #get menu dictionary

    item_dict={}
    item_dict = getItemList(menu_dict,items_ordered, item_dict)
    
    return item_dict

##################################################################################
#  Explanation: Function for column 6. 
#  Summary: Get tax rate for order.
#################################################################################
def get_col_6(tax_list,tup):
    rnum = get_rand_ran(tup)
    tax = tax_list[rnum]
    return tax
##################################################################################
#  Explanations: Functions for column 7.
#  Summary: Get receipt total based on equation:
#           receipt = tax *(N items)
#################################################################################

#Get the total from the dictionary values
#Since we need precision use Decimal
def getDictTotal(item_dict):
    values_list = item_dict.values()
    total = Decimal(0)
    for value in values_list:
        num = Decimal(value)
        total += num
    return total

def get_col_7(item_dict, tax):
    item_total = getDictTotal(item_dict)
    item_total = round(item_total, 2)

    #convert to decimal
    tax = Decimal(tax)
    item_tax =  item_total* tax
    #round number to closest two decimal places
    item_tax = round(item_tax,2)

    total = item_total + item_tax
    return total

##################################################################################
#  Explanation: Functions for column 9
#  Summary: Get random customer id by first finding a random index. Then    
#           getting the customer id from the customer_id_list.
#################################################################################

def get_col_9(tup, customer_id_list):
    rnum = get_rand_ran(tup)
    customer_id = customer_id_list[rnum]
    return customer_id