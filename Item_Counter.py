names = open('names.txt', 'r')
counter = int(0)
for line in names:
    counter+=1
print('There are', counter, 'names')
