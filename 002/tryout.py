print ('Welcome to bla bla calculator')

total_bill = float(input('What was the total bill? $'))
numberof_people = int(input('How many people to split the bill?'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15?')) / 100

x = (total_bill / numberof_people)

last = ((x * tip_percentage) + x)
print("Each person should pay:  $",round(last, 2))

# I did before wathing the videoss yeyyy
