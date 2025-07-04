import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
mean_of_temp = data["temp"].mean()
max_of_temp = data["temp"].max()


monday = data[data.day == "Monday"]
temp_in_farah = (monday.temp * (9/5)) + 32

#create a dataframe from scratch
new_data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

new_data = pandas.DataFrame(new_data_dict)
new_data.to_csv("new_data.csv")
print(new_data)