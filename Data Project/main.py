import csv
import pandas


# with open('weather_data.csv') as file_data:
#     data = csv.reader(file_data)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
# print(temperature)

data = pandas.read_csv('weather_data.csv')
monday = data[data.day == 'Monday']
print(monday['temp'][0])
