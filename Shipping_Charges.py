weight = float(input('Enter the package weight: '))

if weight > 10:
    price = float(4.75)
elif weight > 6:
    price = float(4.00)
elif weight > 2:
    price = float (3.00)
elif weight <= 2:
    price = float(1.50)


print('The price is $',price)
