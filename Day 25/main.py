import pandas as pd
import csv

data = pd.read_csv("Squirrel_Data.csv")
colorDict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [0,0,0]
}

colors = data["Primary Fur Color"]

for color in colors:
    if color == "":
        pass
    elif color == "Gray":
        colorDict["Count"][0] += 1
    elif color == "Cinnamon":
        colorDict["Count"][1] += 1
    elif color == "Black":
        colorDict["Count"][2] += 1

dataset = pd.DataFrame(colorDict, index=[0, 1, 2])
print(dataset)
with open("squirrel_count.csv", "w") as count:
    dataset.to_csv("squirrel_count.csv")

# with open("weather_data.csv") as weatherData:
#     weatherData = weatherData.read()
#     print(weatherData)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data[data.temp == data.temp.max()].day)
# print(data[data.day == "Monday"].temp)
# print((data[data.day == "Monday"].temp)*2+30)
