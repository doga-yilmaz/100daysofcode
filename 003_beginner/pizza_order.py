size = input("What size pizza do you want? S, M or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? \n")
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill = 17
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill = 23
elif size =="L":
    bill = 25
    if add_pepperoni == "Y":
        bill = 28
else:
    print("Use just S, M or L please!")

if extra_cheese == "Y":
    bill += 1

print (f"Your bill is:  ${bill}.")

# it's working but looking like a mess :), time to see angela's solutions.


