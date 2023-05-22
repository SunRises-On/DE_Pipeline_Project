from variables import delivery_list, country_code_iso3, RECORDS, REC_PER_DATE, vendor_dict, customer_id_list, tax_list\
, column_names, vendor_id_ran, delivery_ran, item_ran, customer_id_ran \

from util import increment_date, get_csv_from_dict, get_delivery_method, get_items, get_rand_ran, tax_ran, get_tax\
,get_customer_id

from item import Item
from receipt import Receipt

def insert(column_names, column_values, cur):
    query = f"""INSERT INTO user_purchase
    ({column_names})
    VALUES
    ({column_values});
    """
    #execute the INSERT statement
    try:
        cur.execute(query)
    except Exception as e:
        print(e)

def populate(cursor):
    for i in range(1,RECORDS):
    
        #get vendor id
        vendor_id= get_rand_ran(vendor_id_ran)
    
        #pickup or delivery
        delivery_method = get_delivery_method(delivery_list, delivery_ran)
        
        #items ordered
        items = []
        items = get_items(vendor_id, item_ran, vendor_dict)
        csv_items = get_csv_from_dict(items)

        #date for order
        if((i%REC_PER_DATE) == 0):
            date_obj = increment_date(date_obj)

        #get tax rate
        tax = get_tax(tax_list, tax_ran)
    
        #get receipt total 
        receipt = Receipt(items, tax)
        total = receipt.total
    
        #get customer id number
        customer_id = get_customer_id(customer_id_ran, customer_id_list)
    
        column_values = f""" {vendor_id} , '{delivery_method}' ,
          '{csv_items}' ,'{date_obj}' ,{tax} ,{total} ,'{country_code_iso3}', {customer_id}"""

        insert(column_names, column_values, cursor)

    return cursor
