years = int(input('input number of years: '))
months = 12
monthCounter = 0
totalRainfall = float(0)

for year in range(years):
    for month in range (months):
        monthCounter = monthCounter + 1
        print('Enter the inches of rainfall for month', monthCounter)
        rain = float(input())
        totalRainfall = totalRainfall + rain

print('Total Months:', monthCounter)
print('Total Inches of Rainfall:', totalRainfall)
print('Average Rainfall Per Month:', (totalRainfall/monthCounter))
