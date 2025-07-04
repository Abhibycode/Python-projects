print("Hello, Welcome Tip Calculator")
Bill = float(input("What is your total bill?\n"))
Tip = float(input("What percentage of tip you like to give? 10 12 15\n"))
split = int(input("How many people will split the bill?\n"))
bill_with_tip = Tip /100 * Bill + Bill
amount = str(bill_with_tip/split)
print("Your total bill is: " + amount)