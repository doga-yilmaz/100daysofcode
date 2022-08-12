print ("WELCOME TO THE ROLLER COASTER")

height = int(input("Enter your height..: \n"))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age plase \n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print ("Adult tickets are $12")

    wants_photo = input ("Do you want a photo taken? Y or N.  \n")
    if wants_photo == "Y":
        bill += 3
    
    print(F"Your final bill is ${bill}")

else:
    print("You are not eligible to ride roller coaster")
