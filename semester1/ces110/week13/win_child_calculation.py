
def calc_wind_child(temp, wspeed):
    wind_child= (35.74+0.6215*temp)-(35.75*(wspeed**0.16))+(0.4275*temp)*(wspeed**0.16)
    return wind_child

def convert_fahre(temp):
     temp_f=(temp*9/5)+32
     return temp_f

temp=float(input('What is the temperature? '))
type_temp=input('Fahrenheit or Celsius (F/C)? ')

wind_speed=0
if type_temp.upper()=='C':
    temp_f=convert_fahre(temp)
else:
    temp_f=temp

for i in range(5,60,5):
    wind_speed=i
    wind_child=calc_wind_child(temp_f, wind_speed)
    print(f'At temperature {temp_f:.1f}F, and Wind speed {wind_speed} mph, the windchill is: {wind_child:.2f}')

    
