# import colorgram
#
#
# colors = colorgram.extract("hirspaint.jpg", 30)
# rgb_colors = []
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
t.bgcolor("black")
turtle = t.Turtle()
turtle.penup()
colors_list = [(246, 243, 239), (247, 241, 244), (202, 166, 109), (240, 246, 241), (236, 239, 244), (153, 73, 47), (170, 152, 42), (222, 202, 137), (53, 93, 124), (136, 32, 22), (133, 163, 184), (48, 118, 87), (199, 92, 71), (16, 97, 75), (101, 73, 75), (67, 47, 41), (147, 178, 148), (164, 142, 156), (234, 177, 165), (56, 46, 49), (130, 28, 32), (184, 205, 173), (41, 60, 72), (81, 146, 125), (184, 87, 92), (31, 78, 84), (48, 64, 81), (21, 69, 63), (219, 175, 178), (109, 124, 150)]

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(30, random.choice(colors_list))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()





