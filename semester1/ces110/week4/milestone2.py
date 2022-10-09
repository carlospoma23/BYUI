print("Welcome to the meal calculator. Please enter the following ")
price_meal_child =float(input("\nWhat is the price of a child's meal? "))
price_meal_adult =float(input("What is the price of a adult's meal? "))
price_dessert=int(input('What is the price for each chocolate dessert? '))
price_small_drink=int(input('What is the price for the small drink? '))
price_medium_drink=int(input('What is the price for the medium drink? '))
price_large_drink=int(input('What is the price for the large drink? '))
number_children=int(input('How many children are there? '))
number_adults=int(input('How many adults are there? '))
number_dessert=int(input('How many people want to order dessert? '))
number_sdrink=int(input('How many people want to order small drink? '))
number_mdrink=int(input('How many people want to order medium drink? '))
number_ldrink=int(input('How many people want to order large drink? '))

sales_tax_rate=float(input('What is the sales tax rate? '))

#calculations
subtotal_children=price_meal_child*number_children
subtotal_adults=price_meal_adult*number_adults
subtotal_dessert=price_dessert*number_dessert
subtotal_drink=(price_small_drink*number_sdrink)+(price_medium_drink*number_mdrink)+(price_large_drink*number_ldrink)

subtotal_gen=subtotal_children+subtotal_adults+subtotal_dessert+subtotal_drink
sales_tax=(subtotal_gen)*sales_tax_rate/100
total=subtotal_gen+sales_tax

#outout
print(f'\nSubtotal:   ${subtotal_gen:.2f}')
print(f'Sales tax:    ${sales_tax:.2f}')
print(f'Total:        ${total:.2f}')
print()
amount_payment=float(input('What is the payment amount? '))
change=amount_payment-total
print(f'\nChange: ${change:.2f}')
print("\nThanks for visiting us.")

