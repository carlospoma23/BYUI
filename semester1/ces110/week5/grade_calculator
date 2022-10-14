print('Grade Calculator')
print('___________________________')
print()
grade=int(input('Please enter your grade: '))

#Calculations
if(grade>=90):
    result='A'
elif(grade>=80):
    result='B'
elif(grade>=70):
    result='C'
elif(grade>=60):
    result='D'
else:
    result='F'

#strech 1
sign=" "
last_digit=grade%10

if last_digit>=7:
    sign="+"
elif last_digit<3:
    sign="-"
else:
    sign=" "
if grade>=93:
    sign=" "
if result=="F":
    sign=" "

print(f'The correnpondig letter for your grade is: {result}{sign}')
print()
if (grade>=70):
    print('Congratulations, You passed the course!')
else:
    print("You did not pass the course, Please don't  be discouraged. You can do it!")
