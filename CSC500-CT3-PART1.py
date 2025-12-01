#Get meal amount
meal_cost = float(input('Enter cost of meal here: '))

#Calculate tip, tax, and total price
tip = meal_cost * 0.18
tax = meal_cost * 0.07
total_price = meal_cost + tip + tax

#Output the tip, tax, and total price
print('The meal cost you ${:.2f}.'.format(meal_cost))
print('The tip amount is ${:.2f}.'.format(tip))
print('The tax amount is ${:.2f}.'.format(tax))
print('The total cost is ${:.2f}.'.format(total_price))
