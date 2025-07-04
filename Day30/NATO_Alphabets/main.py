import pandas

data_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data_dict.iterrows()}

def generate_phonetic():
    word = input("Enter a name    ").upper()
    try:
        output_list = [nato_dict[new_item] for new_item in word]
    except KeyError:
        print("Sorry, please enter alphabet")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()