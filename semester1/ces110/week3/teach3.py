
from cmath import pi


side_square=float(input('What is the length of a side of the square ? '))
print(f'The area of the square is : {side_square**2}')
length_rec=float(input('\nWhat is the length of rectangle? '))
width_rec=float(input('What is the width of rectangle? '))
print(f'The area of the rectangle is : {length_rec*width_rec}')
radius_cir=float(input('\nWhat is the radius of the circle? '))
print(f'The area of the circle is : {pi*(radius_cir**2)}')
