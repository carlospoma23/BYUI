from datetime import datetime
import math
current_date=datetime.now()

tire_width_list=[135,145,155,165,175,185,195,205,215,225,235,245,255,258,265,275,285,295,305,315,325,335,345,355,365,375]
tire_ratio_list=[20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
wheel_diameter_list=[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

print('Welcome to the tire store')

validate=True

while(validate==True):
    tire_width=float(input('Enter the width of the tire in mm (ex 205): '))
    if  (tire_width in tire_width_list):
        validate=False
    else:
        print('Please enter a correct value, please verify  your enter data in the next list:')
        print(tire_width_list)
        validate=True


validate=True

while(validate==True):
    tire_ratio=float(input('Enter the aspect ratio of the tire (ex 60): '))
    if  ( tire_ratio in tire_ratio_list):
        validate=False
    else:
        print('Please enter a correct value, please verify  your enter data in the next list:')
        print(tire_ratio_list)
        validate=True


validate=True

while(validate==True):
    wheel_diameter=float(input('Enter the diameter of the wheel in inches (ex 15): '))
    if  ( wheel_diameter in wheel_diameter_list):
        validate=False
    else:
        print('Please enter a correct value, please verify  your enter data in the next list:')
        print(wheel_diameter_list)
        validate=True


# calculing the Tire's price
if tire_width>=135 and tire_width<= 195:
    fw=0.3
elif tire_width>=205 and tire_width<= 295:
    fw=0.8
else:
    fw=1.2

if tire_ratio>=20 and tire_ratio<=55:
    fr=0.4
else:
    fr=0.9

if wheel_diameter>=12 and wheel_diameter <= 20:
    fd=0.4
else:
    fd=0.8
total_price= 120 +300*fw*fr*fd


r1=(((math.pi)*(tire_width**2)*(tire_ratio)))
r2=((tire_width*tire_ratio)+(2540*wheel_diameter))

volume=r1*r2/10000000000

print(f'The approximate volume is {volume:.2f} liters')
print(f'The price for one Tier is {total_price}')


answer_user= input(f'Would you like to buy the tire with those parameters ({tire_width:.0f}/{tire_ratio:.0f}R{wheel_diameter:.0f}) yes/no :?')

if answer_user=='yes':
    phone=input('Please enter your phone number :')
    print('The tire was sold out.')
    with open("tire_volume.txt", "at") as tire_volume_file:
        print(f'{current_date:%Y-%m-%d}, {tire_width}, {tire_ratio}, {wheel_diameter}, {volume:.2f},{phone}', file=tire_volume_file)
else:
    print('Please come back soon, we are here to help.')

