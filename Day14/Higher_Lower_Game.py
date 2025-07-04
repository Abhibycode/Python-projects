import random
import time
from data_set import data
from os import system

def get_data(data):
    score = 0
    while True:
        first_name = random.choice(list(data.keys()))
        first_name_data = data[first_name]

        second_name = random.choice([name for name in data if name != first_name])
        second_name_data = data[second_name]

        print(f"A. {first_name} is {first_name_data[0]}\n\n\nVS\n\n\nB.{second_name} is {second_name_data[0]}\n\n\n\n")
        
        while True:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            if user_choice in ['A', 'B']:
                break
            else:
                print("Invalid input. Please type 'A' or 'B'.")

        answer = ""
        if first_name_data[1] > second_name_data[1]:
            answer = "A"
        else:
            answer = "B"
        
        if user_choice.lower() == answer.lower():
            score += 1
            print(f"you guessed right {answer} as more followers")
            print(f"You score is {score}")
            time.sleep(2)
            system('cls' if system == 'nt' else 'clear')
        
        else:
            print("You lost")
            print(f"Your final score is {score}")
            break


get_data(data)