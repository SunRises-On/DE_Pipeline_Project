from variables import delivery_list, country_code_iso3, RECORDS, REC_PER_DATE, vendor_dict, customer_id_list, tax_list\
, column_names, vendor_id_ran, delivery_ran, item_ran, customer_id_ran \

from util import increment_date, get_csv_from_dict, get_col_3, get_item_dict, get_rand_ran, tax_ran, get_col_6\
,get_col_7, get_col_9


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
        col_2 = get_rand_ran(vendor_id_ran)
    
        #pickup or delivery
        col_3 = get_col_3(delivery_list, delivery_ran)
        
        #items ordered
        item_dict = get_item_dict(col_2, item_ran, vendor_dict)
        col_4 = get_csv_from_dict(item_dict)
    
        #date for order
        if((i%REC_PER_DATE) == 0):
            date_obj = increment_date(date_obj)

        col_5=date_obj

        #get tax rate
        col_6 = get_col_6(tax_list, tax_ran)
    
        #get receipt total 
        col_7 =get_col_7(item_dict, col_6)
    
        col_8=country_code_iso3

        #get customer id number
        col_9 = get_col_9(customer_id_ran, customer_id_list)
    
        column_values = f" {col_2} , '{col_3}' , '{col_4}' ,'{col_5}' ,{col_6} ,{col_7} ,'{col_8}', {col_9}"

        insert(column_names, column_values, cursor)

    return cursor
