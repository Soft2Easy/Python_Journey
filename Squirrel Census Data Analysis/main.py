import pandas
import csv

data_ = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

print(f'Black Squirrel : {data_[data_["Primary Fur Color"] == "Black"].size}')
print(f'Gray Squirrel : {data_[data_["Primary Fur Color"] == "Gray"].size}')
print(f'Cinnamon Squirrel : {data_[data_["Primary Fur Color"] == "Cinnamon"].size}')

black_ = data_[data_["Primary Fur Color"] == "Black"].size
gray_ = data_[data_["Primary Fur Color"] == "Gray"].size
cinnamon_ = data_[data_["Primary Fur Color"] == "Gray"].size

squirrel_dict = {
    'Fur Color': ['Black', 'Gray', 'Cinnamon'],
    'Count': [black_, gray_, cinnamon_]
}

new_data_ = pandas.DataFrame(squirrel_dict)
new_data_.to_csv('new_squirrel_data.csv')
print(new_data_)
