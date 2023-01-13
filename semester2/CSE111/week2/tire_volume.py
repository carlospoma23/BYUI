from datetime import datetime
import math

def main():
    print()
    print('WELCOME TO THE  TIRE STORE ')
    print('____________________________')
    done=False
    while(done==False):
        print()
        print('1. Buy a new tire')
        print('2. Show discounts')
        print('3. Exit')

        user_choice= input('Please enter a option: ')
        print()
        match user_choice:
            case "1":
                print("You chose the option to buy a Tire, Please enter the following parameters :")
                print()
                buying_tire()
                done=False
            case "2":
                print('These are all our discounts')
                print("_____________________________")
                show_discount()
                done=False
            case "3":
                print("Thank you. Goodbye")
                done=True
            case _:
                print("please enter a choice from the menu (1-3).")
                print()
        
def buying_tire():
    current_date=datetime.now()
    #Declaration of lists to store the values of both width, ratio and diameter of the Tire.
    tire_width_list=[135,145,155,165,175,185,195,205,215,225,235,245,255,258,265,275,285,295,305,315,325,335,345,355,365,375]
    tire_ratio_list=[20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
    wheel_diameter_list=[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    tire_width=None
    tire_ratio=None
    wheel_diameter=None

    tire_width_valid=int(validate('Enter the width of the tire in mm (ex 205): ',tire_width,tire_width_list))
    tire_ratio_valid=int(validate('Enter the aspect ratio of the tire (ex 60): ',tire_ratio,tire_ratio_list))
    wheel_diameter_valid=int(validate('Enter the diameter of the wheel in inches (ex 15): ',wheel_diameter,wheel_diameter_list))

    # calculating the Tire's price
    sell_price_tire=price_tire_calculate(tire_width_valid,tire_ratio_valid,wheel_diameter_valid)

    
    # Calculating the Tire's volume 
    r1=(((math.pi)*(tire_width_valid**2)*(tire_ratio_valid)))
    r2=((tire_width_valid*tire_ratio_valid)+(2540*wheel_diameter_valid))
    volume=r1*r2/10000000000
    print('_________________________________________________')
    print()
    print(f'The approximate volume is {volume:.2f} liters')
    print(f'The price for ONE TIRE is {sell_price_tire:.2f} dollars')
    print('_________________________________________________')

    print(f'Your TIRE has those parameters ({tire_width_valid:.0f}/{tire_ratio_valid:.0f}R{wheel_diameter_valid:.0f})')
    print()
    n_tires=int(input("How many TIRES do you want to buy ? "))
    subtotal=int(n_tires)*float(sell_price_tire)
    total_discount=calculating_discount(n_tires,sell_price_tire)
    total=subtotal-total_discount
    print('___________________________________________________')
    print(f'Sub Total : {subtotal:.2f}')
    print(f'Discount  : {total_discount:.2f}')
    print(f'Total     : {total:.2f}    ')
    print('___________________________________________________')
    

    answer_user= input(f'Would you like to buy {n_tires} the TIRE(S) with those parameters ({tire_width_valid:.0f}/{tire_ratio_valid:.0f}R{wheel_diameter_valid:.0f}) yes/no :?')

    if answer_user=='yes':
        phone=input('Please enter your phone number (XXX) XXX-XXXX :')
        print

        print('The tire was sold out.')
        print('**************************************************')
        with open("tire_volume.txt", "at") as tire_volume_file:
            print(f'{current_date:%Y-%m-%d}, {tire_width_valid}, {tire_ratio_valid}, {wheel_diameter_valid}, {volume:.2f},{phone}', file=tire_volume_file)
    else:
        print('Please come back soon, we are here to help.')



def show_discount():
  
    print("You have 0% off if your Buy 1 Tires")
    print("You have 5% off if your Buy 2 Tires")
    print("You have 9% off if your Buy 3 Tires")
    print("You have 12% off if your Buy 4 Tires")




def calculating_discount(number, price):
    
    if number==1:
        rate=0
    elif number==2:
        rate=0.05
    elif number==3:
       rate=0.09
    else:
        rate=0.12

    subtotal=float(number)*float(price)
    discount=subtotal*rate
    return discount




def price_tire_calculate(width, ratio, diameter):
    # calculating the selling price of the tire. The price based on the different parameters entered.
    #the factors used to calculate the sale price are not real, they have been used only for the exercise.
    if width>=135 and width<= 195:
        fw=0.1
    elif width>=205 and width<= 295:
        fw=1.3
    else:
        fw=2.4

    if ratio>=20 and ratio<=55:
        fr=0.1
    else:
        fr=0.3

    if diameter>=12 and diameter <= 20:
        fd=0.1
    else:
        fd=0.8

    purchase_price= 40 + 40*fw + 40*fr +40*fd
    profit=1.7*purchase_price
    sale_price= purchase_price+profit
    return sale_price

def validate(question,number, list):
    valid=True
    while (valid==True):
        number=int(input(f"{question}"))
        if(number in list):
            valid=False
        else:
            valid=True
            print('Please enter a correct value, please verify  your enter data in the next list:')
            print(list)
    return number

main()


