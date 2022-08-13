import random
from unicodedata import name

names = input("Please enter the names with ',' and space : ")
name_list = names.split(", ")

luck_boy = random.choice(name_list)

print(f"{luck_boy} is going to pay...")
