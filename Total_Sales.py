dailySales = [0]*7
counter = int(0)
totalSales = float(0)

while counter < len(dailySales):
    print('Enter sales for day', counter+1)
    dailySales[counter] = float(input())
    counter += 1
    
for sales in dailySales:
    totalSales += sales
print('The total sales for the week are', totalSales)
