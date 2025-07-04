import time
from os import system

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

def is_resource_sufficient(order_ingredients):
    """Checks if there are enough resources to make the drink."""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins(cost):
    """Prompts the user to insert coins and calculates the total amount."""
    print(f"Please insert coins. The cost is ${cost:.2f}")
    while True:
        try:
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickels = int(input("How many nickels? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01
            total_amount = quarters + dimes + nickels + pennies
            return total_amount
        except ValueError:
            print("Invalid input. Please enter a whole number for the number of coins.")

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")
    time.sleep(2)
    system('cls')

def main():
    """The main function to run the coffee machine."""
    while True:
        coffee = input("What would you like? (expresso/latte/cappuccino/report/off) ").lower()

        if coffee == "off":
            print("Turning off machine...")
            break
        elif coffee == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['beans']}g")
        elif coffee in price:
            cost = price[coffee]
            ingredients = {}
            if coffee == "expresso":
                ingredients = {"water": 50, "beans": 18}
            elif coffee == "latte":
                ingredients = {"water": 200, "milk": 150, "beans": 24}
            elif coffee == "cappuccino":
                ingredients = {"water": 250, "milk": 100, "beans": 24}

            if is_resource_sufficient(ingredients):
                payment = process_coins(cost)
                if payment >= cost:
                    change = round(payment - cost, 2)
                    print(f"Here is ${change:.2f} in change.")
                    make_coffee(coffee, ingredients)
                else:
                    print(f"Sorry that's not enough money. Money refunded.")
                    time.sleep(1)
                    system('cls')
            else:
                time.sleep(1)
                system('cls')
        else:
            print("Invalid selection. Please choose from the menu.")
            time.sleep(1)
            system('cls')

if __name__ == "__main__":
    main()