price_meal_child =float(input("What is the price of a child's meal? "))
price_meal_adult =float(input("What is the price of a child's meal? "))
number_children=int(input('How many children are there? '))
number_adults=int(input('How many adults are there? '))
sales_tax_rate=float(input('What is the sales tax rate? '))

#calculations
subtotal_children=price_meal_child*number_children
subtotal_adults=price_meal_adult*number_adults
subtotal_gen=subtotal_children+subtotal_adults
sales_tax=(subtotal_gen)*sales_tax_rate/100
total=subtotal_gen+sales_tax
#outout
print(f'\nSubtotal:   ${subtotal_gen}')
print(f'Sales tax:    ${sales_tax}')
print(f'Total:        ${total}')
print()
amount_payment=float(input('What is the payment amount? '))
change=amount_payment-total
print(f'Change: ${change}')

