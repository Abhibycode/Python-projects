from prettytable import PrettyTable, ALL

table = PrettyTable()

table.title = "Table of famous instagram personality"
table.field_names = ["Name", "Profession", "Number of followers(In Millions)"]
rows_to_be_added = [
    ["Instagram", "Social Media App", 687.7],
    ["Cristiano Ronaldo", "Footballer", 652.7],
    ["Lionel Messi", "Footballer", 505.1],
    ["Selena Gomez", "Singer/Actress", 420.9],
    ["Dwayne Johnson", "Actor/Wrestler", 394.3],
    ["Kylie Jenner", "Actress/Internet Personality", 393.3],
    ["Arian Grande", "Singer/Actress", 375.9],
    ["Kim Kardashian", "Actress/Internet Personality", 357.1],
    ["Beyonce", "Singer", 311.8],
    ["Khloe Kardashian", "Internet Personality", 303.4]
]

table.add_rows(rows_to_be_added)

table.add_row(["Nike", "Sports Brand", 301.3])

for _ in table.field_names:
    table.align[_] = "l"

table._hrules = ALL

print(table)