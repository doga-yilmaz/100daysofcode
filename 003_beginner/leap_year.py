year = int(input("Which year do you want to check? "))

#by_4 = year % 4   # if even it's a LEAP
#by_100 = year % 100 # if even NOT LEAP
#by_400 = year % 400 # if even LEAP

if year % 4 == 0 :
    if year % 100 == 0 : 
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
    
