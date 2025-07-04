from os import system

biding = {}

def biding_app():
    while True:
        name = input("Enter your name    ")
        bid = int(input("Enter your bid $  "))
        biding[name] = bid

        new_bid = input("Are there any new bidders (Yes/No)    ").lower()
        if new_bid != "yes":
            break
        
    system("cls")

    winner = ""
    highest_bidder = 0
    for bidder, bid_amount in biding.items():
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner =  bidder
    
    print(f"The winner is {winner} with ${highest_bidder} bid")

biding_app()