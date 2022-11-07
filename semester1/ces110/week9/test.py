
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

p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

