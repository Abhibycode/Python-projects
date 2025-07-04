import pandas

data_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data_dict.iterrows()}

word = input("Enter a name    ").upper()

output_list = [nato_dict[new_item] for new_item in word]
print(output_list)