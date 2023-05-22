#where I keep all my fake data variables
from Resources.restaurant_menu import McDonald_menu, Wingstop_menu, Taco_bell_menu
#Python imports
import datetime


def create_date_obj(year, month, day):
    date_obj = datetime.datetime(year, month, day)
    return date_obj


delivery_list = ['pickup', 'delivery']
country_code_iso3 = 'USA'
RECORDS = 12001
REC_PER_DATE = 100
YEAR = 2023
MONTH = 1 
DAY = 1
vendor_dict = { 1: McDonald_menu,
             2: Wingstop_menu,
             3: Taco_bell_menu}


customer_id_list = list(range(1,10001))

tax_list = [0,.029,.04,.04225,.0445,.045,.0475,.05,.053,.055,.056,.0575,.06,.061,.0625,.0635,.065,.06625,.0685,.06875,.07,.0725]

col_names="vendor_id, delivery_method, menu_items, invoice_date, tax, total, country_code_iso3, customer_id"



vendor_id_ran = (1,4) # vendor id range
delivery_ran = (0,2) #delivery method range
item_ran =(1,4) #range for items per order
tax_ran=(0, len(tax_list)) #range for tax options
customer_id_ran=(0, 10000) #range for index for customer_id_list