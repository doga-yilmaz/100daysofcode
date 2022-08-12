print ("Welcome to the rollercoaster!")

height = int(input("What is your height in cm : "))

if height >= 120:
    print ("You can use the god damn roller coaster")
    age = int(input("What is your age?"))
    if age < 12 :
        print("Plase pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You cannot use the roller coaster sir !!")