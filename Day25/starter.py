import csv
with open("weather_data.csv")  as data_files:
    data = data_files.readlines()

print(data)

with open("weather_data.csv")  as data_files:
    data = csv.reader(data_files)
    for row in data:
        print(row)