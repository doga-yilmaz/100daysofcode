import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
x = int(len(names))
lucky_number = random.randint(0, x-1)
lucky_boy = names[lucky_number]


print(f"{lucky_boy} is going to buy the meal today!")

# yes yes I did it, but it took longer than it supposed to be



