print('Welcome to the Shopping Cart Program')
done=False
while(done==False):
    print('Please select one of the following:')
    print()
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Exit')
    user_choice= input('Please enter an action: ')

    match user_choice:
        case "1":
            print("Agregando") 
            add_items(list_products)
            break
        case "2":
            print("Visualizando")
            break
        case "3":
            print("Eliminando")
            break
        case "4":
            print("Calculando")
            break
        case "5":
            print("Goodbye")
            done=True
        case _:
            print("Please enter a choice from the menu (1-4).")
            print()
            
list_products=[]
def add_items(input_user, lista=[]): 
    input_user=None   
    while input_user!='quit':
        input_user=input('Please enter the items of the shopping list (type: quit to finish): ')
        if(input_user!="" and input_user!='quit'):
            lista.append(input_user)
    return(lista)

print(add_items(list_products))  
