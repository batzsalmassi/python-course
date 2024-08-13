print('Welcome to the TIP calculator 🥳')
bill = float(input('What was the total bill? $'))
tip = int(input('What precentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
total = bill + (bill * tip / 100) # 100% + tip
each = total / people 
print(f'Each person should pay: ${round(each, 2)}') # round to 2 decimal places