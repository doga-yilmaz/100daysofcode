from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, -50, -10, 30, 70, 100]
all_turtles = []

for i in range(len(colors)):
    jim_the_turtles = Turtle(shape="turtle")
    jim_the_turtles.speed("slowest")
    jim_the_turtles.color(colors[i])
    jim_the_turtles.penup()
    jim_the_turtles.goto(x=-230, y=y_positions[i])
    all_turtles.append(jim_the_turtles)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
