def maximum(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return num1
    elif num1 < num2:
        return num2

numberOne = float(input('Enter the first value to compare: '))
numberTwo = float(input('Enter the second value to compare: '))

print('The highest number is', maximum(numberOne, numberTwo))
