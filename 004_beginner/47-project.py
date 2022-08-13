import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
the_list = [rock, paper, scissors]
choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
#c_choice = the_list.index(random.choice(the_list))
c_choice = random.randint(0,2)

print("\nYou choose:  \n",the_list[choice],"\n Computer chose: ",the_list[c_choice])

if choice < 0 or choice >= 3:
    print("Enter a valid number please!")
elif choice == 0 and c_choice == 1:
    print ("Computer win!")
elif choice == 0 and c_choice == 2:
    print("You win!")
elif choice == 1 and c_choice == 0:
    print("You win")
elif choice == 1 and c_choice == 2:
    print("Computer win!")
elif choice == 2 and c_choice == 0:
    print("Computer win!")
elif choice == 2 and c_choice == 1:
    print("You win")
elif choice == c_choice:
    print("DRAW TRY AGAIN !")

    

# YESSS I DID ITTTTT , NOW LET'S LOOK ANGELA'S SOLUTION.
# My code is 3 line longer but I am not big fan of this game soo.... :))






