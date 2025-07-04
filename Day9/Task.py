travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

for city in travel_log["France"]:
    if city == "Lille":
        print(city)

#OR

print(travel_log["France"][1])



#------------------------------------------------------------------------

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])



#------------------------------------------------------------------------
travel_log_new = {
    "France":{
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log_new["Germany"]["cities_visited"][2])