fullName = str(input('Enter your full name: '))
initials = []
counter = 0

initials.append(fullName[0])

while fullName.find(' ') > 0:
    spaceIndex = fullName.find(' ')
    initials.append(fullName[spaceIndex+1])
    fullName = fullName[:spaceIndex] + fullName[spaceIndex+1:]
    counter+=1
    if counter > 20:
        print('error')
        break

print('Your initials are:')
for initial in initials:
    print(initial.upper(), '. ', sep='', end='')
