
def main():
    print()
    print('Welcome to the Shopping Cart Program')
    done=False 
    list_products=[]
    while(done==False):
        print()
        print('Please select one of the following:')
        print()
        print('1. Add item')
        print('2. View cart')
        print('3. Remove item')
        print('4. Compute total')
        print('5. Quit')
        user_choice= input('Please enter an action: ')
        print()
        match user_choice:
            case "1":
                add_items(list_products)
                done=False
            case "2":
                view_items(list_products)
                done=False
            case "3":
                delete_items(list_products)
                done=False
            case "4":
                total_items(list_products)
                done=False
            case "5":
                print("Thank you. Goodbye")
                done=True
            case _:
                print("Please enter a choice from the menu (1-4).")
                print()
            

def add_items(lista=[]): 
    input_item=None   
    #input_price=None
    while input_item!='quit':
        input_item=input('What item would you like to add?(type: quit to finish): ')
        if(input_item!='quit'):
            input_price=input(f"What is the price of {input_item}? ")
            input_price =validation_number_float(input_price)
        if(input_item!="" and input_item!='quit'):
            lista.append(f'{input_item} - ${input_price:.2f}')
        print(f"'{input_item}' has been added to the cart.")
    return(lista)

def view_items(lista=[]):
    if len(lista)!=0:
        print('The contents of the shopping cart are:')
        for i in range(len(lista)):
            item=lista[i]
            print(f'{i+1} : {item}')
    else:
        print('The shopping cart is empty. please select 1. Add item ')    
    return lista       

def total_items(lista=[]):
    total=0
    price=0
    temp_list=[]
    if(len(lista)!=0):
        for item in lista:
            temp_list=item.split(' - $')
            price=float(temp_list[1])
            total+=price
        print(f'The total price of the items in the shopping cart is ${total:.2f}')
    else:
        print('The shopping cart is empty. please select 1. Add item ')   
    return lista

def delete_items(lista=[]):
    input_item=None
    
    if(len(lista)!=0):
        view_items(lista)
        input_item=input('Which item would you like to remove? ')
        input_item=validation_number_int(input_item)
        for item in range(len(lista)):
            if input_item==item+1:
                lista.pop(item)
        print(f'Item {input_item} has been removed.')
    else:
        print('The shopping cart is empty. please select 1. Add item ') 
    return lista


def validation_number_float(num):
    done=False
    num1=None
    while done==False:
        try:
          num1=float(num)
          done=True
        except ValueError:
         num=input('Please enter a number: ')
    return num1

def validation_number_int(num):
    done=False
    num1=None
    while done==False:
        try:
          num1=int(num)
          done=True
        except ValueError:
         num=input('Please enter a integer number: ')
    return num1

if __name__=='__main__':
  main()



