import turtle
import pandas

names = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


correct_answers = 0
wrong_answers = 0


states = data.state.to_list()

is_game_on = True
while is_game_on:
    answer = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="Write a State Name").title()

    if answer in states:
        correct_answers += 1

        state_coor = data[data.state == answer]
        x_cor = int(state_coor.x)
        y_cor = int(state_coor.y)
        names.penup()
        names.hideturtle()
        names.goto(x_cor, y_cor)
        names.write(answer)
    else:
        wrong_answers += 1
        print(wrong_answers)

    if correct_answers == 50:
        is_game_on = False
    if wrong_answers == 3:
        is_game_on = False



screen.exitonclick()


# Angela's solution certainly better than mine. I could add an exit and a "to learn" list.









