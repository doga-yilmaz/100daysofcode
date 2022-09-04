

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("City Name", ["İstanbul", "Konya", "Ankara", "İzmir", "Antalya", "Adana"])
table.add_column("Population", [174584123, 4120578, 7854963, 9845121, 6248796, 3547891])
table.add_column("Area", [2354, 4586, 1247, 4568, 9870, 5648])
table.align = "l"


print(table)


