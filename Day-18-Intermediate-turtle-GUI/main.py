import turtle as t
import random

tim = t.Turtle()
tim.pensize(10)

colors = ["DeepSkyBlue", "DarkOliveGreen", "GreenYellow", "Magenta", "Orange", "SpringGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):

        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
