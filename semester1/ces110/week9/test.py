
"""Function for sum of 2 numbers
def suma(a, b):    
    sum=a+b
    return(sum)

n1=int(input('ingrese n1: '))
n2=int(input('ingrese n2: '))
  
print(suma(n1, n2))
"""


""" Una excelente funcion para agregar items 
list_products=[]



def add_items(input_user, lista=[]): 
    input_user=None   
    while input_user!='quit':
        input_user=input('Please enter the items of the shopping list (type: quit to finish): ')
        if(input_user!="" and input_user!='quit'):
            lista.append(input_user)
    return(lista)

print(add_items(list_products))  
"""

# ...
# Code here that populates the two lists
# ...

def valid_int_number():
  done=False
  while done==False:
      num=input('escribe un numero ')
      try:
        num=float(num)
        print('Buen trabajo')        
        done=True
      except ValueError:
        print('Por favor escriba un numero')
  return num

valid_int_number()