currentNumber = float(0)
total = float(0);

while currentNumber >= 0:
    total = total + currentNumber
    print('Input a positive number to add to the sum')
    currentNumber = float(input('OR input a negative number to end the program and display the sum: '))

print('The sum is ', total)
