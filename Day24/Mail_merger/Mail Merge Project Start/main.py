#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from idlelib.configdialog import changes
from os import write

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#My solution
# with open(r"./Input/Letters/starting_letter.txt") as letter:
#     original_lines = letter.readlines()
#     print(original_lines)
#
#
# with open(r"./Input/Names/invited_names.txt", mode="r") as invited_name:
#     names = [name.strip() for name in invited_name.readline()]
#     for name in names:
#         change = f"Dear {name.strip()} \n"
#         modified = [change] + original_lines[1:]
#
#         with open(fr"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as new_letters:
#             new_letters.writelines(modified)

PLACEHOLDER = "[name]"

with open(r"./Input/Names/invited_names.txt") as names_in_letter:
    names = names_in_letter.readlines()

with open(r"./Input/Letters/starting_letter.txt", mode="r") as letters:
    letter_content = letters.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(fr"./Output/ReadyToSend/Letter_for_{name.strip()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)