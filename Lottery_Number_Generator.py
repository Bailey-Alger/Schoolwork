import random

lotNum  = [0]*7

for index in range(7):
    lotNum[index] = random.randint(0,9)
    
print('Your lottery numbers are:')
for index in range (7):
    print(lotNum[index], end='')
