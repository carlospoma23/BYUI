
from asyncio.proactor_events import _ProactorDuplexPipeTransport


number1=int(input('What is the first number? '))
number2=int(input('What is the second number? '))

#logical
if (number1>number2):
    print('The first number is greater')
else:
    print('The first number is not4 greater')

if (number1==number2):
    print('The numbers are equal')
else:
    print('the numbers are not equal')

if(number1<number2):
    print('the second number is greater')
else:
    print('that second number is not greater')

print()
animal=input('What is your favorite animal? ')

if (animal.lower()=='bear'):
    print('That is my favorite animal too')
else:
    print('that one is not my favorite.')