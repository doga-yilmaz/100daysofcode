import random


from hangman_words import word_list
choosen_word = random.choice(word_list)

word_length = len(choosen_word)
end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

display = []
for l in range(word_length):
    display.append("_")


while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've aldredy gussed {guess}")

    for i in range(word_length):
        letter = choosen_word[i]
        if letter == guess:
          display[i] = letter

        
    if not guess in choosen_word:    
        lives -= 1
        if lives == 0:
         end_of_game = True
         print("You lose !")
         


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win !")

    from hangman_art import stages
    print(stages[lives])
