import random
from os import system

get_number = random.randint(1, 100)

attempt = 0

def let_guess(attempt):
    while True:
        guess = int(input("Guess a number: \n"))
        if guess > get_number:
            print("To High")
        elif guess < get_number:
            print("To low")
        else:
            print("You guess number right, You won the game!!!")
            break
            
        attempt -= 1
        if attempt == 0:
            print(f"Your are out of attempts, {get_number} was the answer")
            break


def Game():
    print("""  ________                               _______               ___.                 
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/            \/    \/     \/       \n\n\n\n""")


    print("Welcome the Guess the number" \
    "I'm thinking of number between 1 to 100")
    level = str(input("Choose difficulty. Type 'easy' or 'hard':    \n")).lower()


    if level == 'easy':
        attempt = 10
        let_guess(attempt)
    
    elif level == 'hard':
        attempt = 5
        let_guess(attempt)

    start_again = str(input("To start game again. Type 'yes' or 'no':    \n"))

    if start_again == 'yes':
        system("cls")
        Game()
    elif start_again == 'no':
        print("Thanks for visitin, we will see you soon")
    else:
        print("Please enter a valid choice")
        start_again = str(input("To start game again. Type 'yes' or 'no':    "))
    
Game()