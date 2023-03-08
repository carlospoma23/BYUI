import csv
from datetime import datetime
#are the indexes of the elements in products dictionary, each value is a list
PRODUCT_INDEX=0
NAME_INDEX=1
PRICE_INDEX=2

#indexes in request dictionary

QUANTITY_INDEX=1

def main():
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

            products_list=products_dict[code_product]
            name_product=products_list[NAME_INDEX]
            price_product=float(products_list[PRICE_INDEX])
            number_items += request_quantity
            subtotal += price_product*request_quantity

            print(f"{name_product}: {request_quantity}  @ {price_product}")
    
    sales_tax=0.06*subtotal
    total=subtotal+sales_tax
    
    print(f"\nNumber of Items: {number_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    
    print(f"\n Thank you for shopping at the {store_name}")


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