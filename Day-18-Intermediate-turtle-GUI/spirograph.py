import turtle as tt
import random

tt.bgcolor('black')
tt.speed(0)
tt.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap )):
        tt.color(random_color())
        tt.circle(100)
        tt.setheading(tt.heading() + size_of_gap)

draw_spirograph(5)
screen = tt.Screen()
screen.exitonclick()











