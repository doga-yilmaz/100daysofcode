print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input ('You are at a crossroad. Where do you want to go? Type "left" or "right"')

if direction == "left":
    action = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print ("You enter a room of beasts. Game Over.")
        elif door =="yellow":
            print("You win")
        else:
            print("Game over!")
    else:
        print("Attacked by torut. Game over!")
else:
    print("Fall into a hole. Game over!")

## Yeappp I did it...




    
