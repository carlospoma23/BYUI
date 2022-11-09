
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
    input_price=None
    while input_item!='quit':
        input_item=input('What item would you like to add?(type: quit to finish): ')
        if(input_item!='quit'):
            input_price=input(f"What is the price of {input_item}? ")
        validation_number(input_price)
        if(input_item!="" and input_item!='quit'):
            lista.append(f'{input_item} - ${input_price}')
       
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
    view_items(lista)
    if(len(lista)!=0):
        input_item=int(input('Which item would you like to remove? '))
        for item in range(len(lista)):
            if input_item==item+1:
                lista.pop(item)
    else:
         print('The shopping cart is empty. please select 1. Add item ') 
    return lista

def validation_number(num):
    done=False
    num1=0
    while done==False:
        try:
          num1=float(num)
          num.isdigit()
          done=True
        except ValueError:
          print('Please enter a number: ')

    return num1


if __name__=='__main__':
  main()



