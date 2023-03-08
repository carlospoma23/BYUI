import csv

#are the indexes of the elements in products dictionary, each value is a list
PRODUCT_INDEX=0
NAME_INDEX=1
PRICE_INDEX=2

#indexes in request dictionary

QUANTITY_INDEX=1

def main():
    id_product=0

    products_dict=read_dictionary('products.csv',id_product)
    print("ALL PRODUCTS")
    for k,v in products_dict.items():
        print(k,v)

    #reading the CVS request and storing and value in list_request

    list_request=[]

    print()
    print("REQUEST ITEMS")    
    with open('request.csv','rt') as csv_file:
        reader=csv.reader(csv_file)
        next(reader)

        for code, quantity in reader:
            
            list_request.append(code + "," + quantity)
            code_product=code
            request_quantity=quantity

            products_list=products_dict[code_product]
            name_product=products_list[NAME_INDEX]
            price_product=products_list[PRICE_INDEX]



            print(f"{name_product}: {request_quantity}  @ {price_product}")



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