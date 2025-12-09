#Ask for input in years
years = int(input('How many years of rainfall do you want to track?'))
#Set parameters for other variables
months = 12
inchesRain = 0.0

#Create the loop
for month in range(months):
    rain = int(input('How much did it rain that month in inches?'))
    inchesRain += rain

#Set parameters for calculations
numMonths = years * months
averageRain = inchesRain / numMonths

print('The total rain over that period was {:.2f}.'.format(inchesRain))
print('The number of months measures was {}.'.format(numMonths))
print('The average rainfall was {:.2f} inches.'.format(averageRain))
