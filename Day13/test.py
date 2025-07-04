try:
    age = int(input("Enter age:    "))
except ValueError:
    print ("Please enter a number")
    age = int(input("Enter age:    "))

if age > 18:
    print("Adult")