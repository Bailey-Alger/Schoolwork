day = 1
bugsTotal = 0
while day < 8:
    print('Bugs collected day', day, ':')
    bugsToday = int(input())
    bugsTotal = bugsTotal + bugsToday
    day = day + 1
print('The total bugs collected this week is', bugsTotal)
