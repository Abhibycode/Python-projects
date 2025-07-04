import pandas
import csv

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

extracted_data = data["Primary Fur Color"]
print(extracted_data)
gray = extracted_data[extracted_data == "Gray"].size
cinnamon = extracted_data[extracted_data == "Cinnamon"].size
black = extracted_data[extracted_data == "Black"].size

new_dict = {
    "Color": ["gray", "cinnamon", "black"],
    "Count": [gray, cinnamon, black]
}

new_dict = pandas.DataFrame(new_dict)
new_dict.to_csv("squirrel_count.csv")