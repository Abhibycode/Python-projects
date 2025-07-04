print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      
      ''')

print("Welcome to treasure hunt game")
choice1 = str(input("Choose your path wisely, which you want to go? (Left or Right)?\n")).lower()
if choice1 == "left":
    choice2 = str(input("You reached to colombian beach, you need to go to Pumban island\nHowever boar is not available right now\nWhat is your choice?(Wait/Swim)\n")).lower()
    if choice2 == "wait":
        choice3 = str(input("Excellent choice, you got saved from sharks\nNow you have three door and treasure behind one of them\nChoose wisely or you will face consquence (Blue/Yellow/Red)")).lower()
        if choice3 == "blue":
            print("You won the game!!!!")
        elif choice3 == "yellow":
            print("There is sewer behind this door, You lost\nGame Over")
        else:
            print("There was dragon behind it, It toasted you\nGame Over")
    else:
        print("You are eaten by shark, Game Over!!!")
else:
    print("You fallen in hole\nGame Over!!!")