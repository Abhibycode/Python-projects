import random

choices = ["rock", "paper", "scissors"]

user_choice = str(input("Please enter your choice: (Rock/Paper/Scissors)")).lower()
random_choice = random.randint(0, len(choices)-1)
computer_choice = choices[random_choice]

if user_choice == "rock":
    if computer_choice == "rock":
        print("User Choice: \n")
        print("""       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
              """)
        print("\nComputer Choice: \n")
        print("""       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
              """)
        print("\nIt's draw")

    elif computer_choice == "scissors":
        print("User Choice: \n")
        print("""       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
              """)
        print("\nComputer Choice: \n")
        print("""       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | |      
        \__(__|""")
        print("\nRock smashed scissor, You Won!!!\n")

    else:
        print("User Choice: \n")
        print("""       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
              """)
        print("\nComputer Choice: \n")
        print("""         /"\
     /"\|\./|/"\
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |/"\
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |""")
        print("\nFist stopped rock, You Lost\n")


elif user_choice == "scissors":
    if computer_choice == "scissors":
        print("User Choice: \n")
        print("""       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | | 
        \__(__|""")
        print("\nComputer Choice: \n")
        print("""       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | |
        \__(__|""")
        print("\nScissors broke Scissors, It's Draw\n")

    elif computer_choice == "rock":
        print("User Choice: \n")
        print("""       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | | 
        \__(__|""")
        print("\nComputer Choice: \n")
        print("""       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
              """)
        print("\nScissors got smashed by rock, You Lost\n")

    else:
        print("User Choice: \n")
        print("""       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | | 
        \__(__|""")
        print("\nComputer Choice: \n")
        print("""         /"\
     /"\|\./|/"\
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |/"\
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |""")
        print("\nScissors cuts paper, You Won!!!\n")



else:
    if computer_choice == "scissors":
        print("User Choice: \n")
        print("""         /"\
     /"\|\./|/"\
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |/"\
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |""")
        print("\nComputer Choice: \n")
        print("""       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \
      \,)   | |     
        \__(__|""")
        print("\nPaper got cut scissor, You Lost!!!\n")
    
    elif computer_choice == "rock":
        print("User Choice: \n")
        print("""         /"\
     /"\|\./|/"\
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |/"\
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |""")
        print("\nComputer Choice: \n")
        print("""       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
              """)
        print("\nPaper stopped rock, You Won!!!\n")

    else:
        print("User Choice: \n")
        print("""         /"\
     /"\|\./|/"\
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |/"\
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |""")
        print("\nComputer Choice: \n")
        print("""         /"\
     /"\|\./|/"\
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |/"\
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |""")
        print("\nPaper stopped Paper, You Draw!!!\n")