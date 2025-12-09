#Ask for number of books purchased this month
purchases = int(input('Enter number of books purchased this month:'))

#Create if, else if, and else conditions and print the results
if 0 <= purchases < 2:
    print('You earned 0 points')
elif 2 <= purchases < 4:
    print('You earned 5 points')
elif 4 <= purchases < 6:
    print('You earned 15 points')
elif 6 <= purchases < 8:
    print('You earned 30 points')
elif purchases >= 8:
    print('You earned 60 points')
else:
    print('Incorrect number of books entered.')
