from datetime import datetime


def main():
    
    subtotal=float(input('Please enter the subtotal: '))

    #Calculing discount
    discount=calc_discount(subtotal)
    
    subtotal_w_discount=subtotal-discount
    taxes=0.06*subtotal_w_discount

    total=subtotal_w_discount+taxes

    print(f'Discount amount: {discount:.2f}')
    print(f'Sales tax amount: {taxes:.2f}')
    print(f'Total {total:.2f}')

    
def calc_discount(subtotal):

    current_day_time=datetime.now()
    current_day=current_day_time.weekday()
    disc_rate=0.10

    if (current_day==1 or current_day==2) and (subtotal>=50):
        
        discount=subtotal*disc_rate
    else:
        discount=0
    
    return discount


main()
