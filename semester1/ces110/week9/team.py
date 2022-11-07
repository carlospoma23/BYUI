numbers=[]
print('Enter a list of numbers, Type 0 when finished. ')
number_input=None
while(number_input!=0):
    number_input=int(input('Enter number : '))
    if (number_input!=0):
        numbers.append(number_input)

sum=0
average=0
largest_number=max(numbers)

for number in numbers:
    sum+=number

average=sum/len(numbers)
print(f'The sum is: {sum}')
print(f'The average is: {average}')
print(f'The largest number is: {largest_number}')
positive_list=[]
smallest_pnumber=None
for number in numbers:
    if (number>=0):
        positive_list.append(number)
 
if(len(positive_list)==0):
    print('No hay numeros positivos en la lista')
else:
    smallest_pnumber=min(positive_list)
    print(f'The smallest positive number is: {smallest_pnumber}')

sorted_list=sorted(numbers)
print('The sorted list is :')
for number in sorted_list:
    print(number)

