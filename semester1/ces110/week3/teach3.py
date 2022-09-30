
from cmath import pi

side_square=float(input('What is the length of a side of the square ? '))
print(f'The area of the square is : {side_square**2}')
length_rec=float(input('\nWhat is the length of rectangle? '))
width_rec=float(input('What is the width of rectangle? '))
print(f'The area of the rectangle is : {length_rec*width_rec}')
radius_cir=float(input('\nWhat is the radius of the circle? '))
print(f'The area of the circle is : {pi*(radius_cir**2)}')
print()
#Strech Challenge

user_single_value=float(input("Please enter the length value "))
print(f'The area of the square is {user_single_value**2}')
print(f'The area of the circle  is {pi*(user_single_value**2)}')
print(f'The volume of the cube is {user_single_value**3}')
print(f'The volume of the sphere is {4/3*pi*(user_single_value**3)}')

print()

user_single_value_cm=float(input("Please enter the length value  in centimeters"))
print(f'The area of the square in centimeters is {user_single_value_cm**2} square centimeters')
print(f'The area of the square in meters is {user_single_value**2/10000} square meters')
