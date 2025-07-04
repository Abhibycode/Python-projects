print("Welcome to Python Pizza Deliveries")

size = str(input("What size of pizza you would like to order? (s/m/l)\n"))
bill = 0

if size == "s":
    p = 2
    bill += 15
    pepperoni = str(input("You would like to have pepperoni? (y/n) \n"))
    quantity = int(input("How many pepperoni you want to add? \n"))
    bill += p*quantity

elif size == "m":
    p = 3
    bill += 20
    pepperoni = str(input("You would like to have pepperoni? (y/n) \n"))
    quantity = int(input("How many pepperoni you want to add? \n"))
    bill += p*quantity

else:
    p = 3
    bill += 25
    pepperoni = str(input("You would like to have pepperoni? (y/n) \n"))
    quantity = int(input("How many pepperoni you want to add? \n"))
    bill += p*quantity

print(f"Thanks for your order, you bill is ${bill}")