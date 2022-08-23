import random

### MY SOLUTION 

print ("Welcome to the number guessing game !")
print ("I'm thinking of a number between 1 and 100.")

hard_lives = 5
easy_lives = 10

the_number = random.randint(0,100)
print(f"pssssst {the_number}")

def zıbab (lives):
    end_game = False
    while not end_game:
        print(f"You have {lives} attempts remaining to guess the number. ")
        guess =  int(input("Make a guess: "))
        if the_number == guess:
            print (" You win ! ")
            end_game = True
        elif lives == 1:
            print("GG, game over buddy :( ") 
            end_game = True
        elif guess > the_number:
            print("Too high, guess again !")
            lives -= 1
        elif guess < the_number:
            print("Too low, guess again !")
            lives -= 1 

def the_game():
    hard_or_easy = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if hard_or_easy == 'easy':
        zıbab(lives=easy_lives)
    elif hard_or_easy == 'hard':
        zıbab(lives=hard_lives)

the_game()
