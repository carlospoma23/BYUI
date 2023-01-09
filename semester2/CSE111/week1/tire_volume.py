
import math

tire_width=float(input('Enter the width of the tire in mm (ex 205): '))
tire_ratio=float(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter=float(input('Enter the diameter of the wheel in inches (ex 15): '))


r1=(((math.pi)*(tire_width**2)*(tire_ratio)))
r2=((tire_width*tire_ratio)+(2540*wheel_diameter))

volume=r1*r2/10000000000

print(f'The approximate volume is {volume:.2f} liters')