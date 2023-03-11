import csv
from datetime import datetime
import string, random
#are the indexes of the elements in products dictionary, each value is a list
PRODUCT_INDEX=0
NAME_INDEX=1
PRICE_INDEX=2

#indexes in request dictionary

QUANTITY_INDEX=1

def main():

    try:

        id_product=0
        products_dict=read_dictionary('products.csv',id_product)
        #reading the CVS request and storing and value in list_request
        list_request=[]
        print()
        store_name="Inkom Emporium"
        print(f"**** {store_name} **** \n")
        number_items=0
        subtotal=0

        with open('request.csv','rt') as csv_file:
            reader=csv.reader(csv_file)
            next(reader)
            for code, quantity in reader:
                list_request.append(code + "," + quantity)
                code_product=code
                request_quantity=int(quantity)

            #    if code_product in products_dict:
                products_list=products_dict[code_product]
                name_product=products_list[NAME_INDEX]
                price_product=float(products_list[PRICE_INDEX])
                number_items += request_quantity
                subtotal += price_product*request_quantity

                print(f"{name_product}: {request_quantity}  @ {price_product}")
        
        #genering Coupon random

        number_of_coupon=1
        length_of_coupon=8
        
        for x in range(number_of_coupon):
            coupon=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_coupon))
        
      
       

                
        current_date_time=datetime.now()
        # get a integer number related to the week day (Where Monday is 0 and Sunday is 6)
        current_date=current_date_time.weekday()
        #testing current_date
        #current_date=6
        
        current_time=current_date_time.time()
        currect_hour=current_time.hour
        #testomg current_hour
        #currect_hour=13
    
        discount=0
        #computing discount if is tuesday or wednesday or the time is before 11 am
        if (current_date==1 or current_date==2 or currect_hour<11):
            rate_discount_day=0.10
            discount=rate_discount_day*subtotal
            sales_tax=0.06*(subtotal-discount)
            total=subtotal-discount+sales_tax

        else:
            sales_tax=0.06*(subtotal-discount)
            total=subtotal-discount+sales_tax
            
       
        
        print(f"\nNumber of Items: {number_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f'Discount: {discount:.2f}')
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print(f'\nCOUPON: {coupon}')
        print("***********************")
        print("Please don't forget to use this 'Coupon' the next time and you will receive 5 % off for your purchases.")
    
        print(f"\nThank you for shopping at the {store_name}")
        

        print(f'{current_date_time:%a %b %d   %I:%M:%S   %Y} ')
       
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print(f"Please make sure that the file exist.")
    
    except(csv.Error, KeyError) as error:
        print(error)
        print(f'Error: unknown product ID {error}  of {csv_file.name} line {reader.line_num}')


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary={}
    with open(filename, 'rt') as csv_file:
        reader=csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key=row_list[key_column_index]
            dictionary[key]=row_list
        
    return dictionary


if __name__=="__main__":
    main()