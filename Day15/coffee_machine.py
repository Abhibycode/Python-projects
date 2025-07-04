import time
from os import system

#add data sets

price = {
    "latte": 4.40,
    "cappuccino": 3.50,
    "expresso": 1.70
}

resources = {
    "water": 5000,
    "milk": 3000,
    "beans": 100
}

try:
    coffee = str(input("What would you like? (expresso/latte/cappuccino)    ")).lower()
except TypeError:
    print("Please enter a valid choice")
    
try:
    if coffee in price:
        money = map(float, (input(f"Great choice, {coffee} cost ${price[coffee]})    ")).split())
        total = sum(money)
except TypeError:
    print("Please enter a valid choice")

def check_amount(total):
    if total < price:
        print("Sorry, wasn't sufficient money")
        time.sleep(0.5)
        print(f"Please collect your refund of ${total}")
        
    elif total > price:
        remaining = total - price
        print(f"Here is your ${remaining} in change")
    else:
        print("Thanks for money, we are preparing coffee shortly")
        time.sleep(0.5)
        print("Enjoy your cofee")

def quantity():
    """Checking resources and making coffee and keeping track of resources at same time"""
    if coffee == "expresso":
        if resources["water"] > 30 and resources["beans"] > 9:
            check_amount()
            resources["water"] -= 30
            resources["beans"] -= 9
        else:
            print("Sorry, we are out resources")

    elif coffee == "latte":
        if resources["beans"] > 9 and resources["milk"] > 21 and resources["water"] > 30:
            check_amount()
            resources["beans"] -= 9
            resources["milk"] -= 21
            resources["water"] -= 30
        else:
            print("Sorry, we are out of resources")

    else:
        if resources["beans"] > 20 and resources ["milk"] > 60 and resources["water"] > 60:
            check_amount()
            resources["beans"] -= 20
            resources["milk"] -= 60
            resources["water"] -= 60
        else:
            print("Sorry, we are out of resources")

def mainteance(coffee):
    if coffee == "off":
        print("Turning off machine")
        system("cls")

    elif coffee == "report":
        price(f"Water: {resources["water"]} ml")
        price(f"Coffee: {resources["beans"]} g")
        print(f"Milk: {resources['milk']} ml")
