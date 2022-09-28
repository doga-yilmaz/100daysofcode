# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)




# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data_one = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
#
# average = sum(temp_list) / len(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
## Get Data in Columns
# print(data["condition"])
# print(data.condition)


## Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


## Celsius to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# fahrenheit = (monday_temp * 9/5) + 32

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# created_data = pandas.DataFrame(data_dict)
# print(created_data)
# created_data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

new_dict = {
    "Fur color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}
squirrel_data = pandas.DataFrame(new_dict)
squirrel_data.to_csv("squirrel_color_data.csv")









