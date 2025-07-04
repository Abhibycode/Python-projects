from os import system
import Addition as add
import Substraction as sub
import Multiplication as mul
import Division as div

def Calc():
    num1 = float(input("Enter first number:    "))
    while True:
        operation = input("Enter your choice 1. Addition (+), 2. Substraction (-), 3. Multiplication (*), 4. Division (/), or 'q' to quit: ")
        if operation == 'q':
            system("cls")
            break
        num2 = float(input("Enter second number:    "))
        if operation == "+" or operation == "addition":
            num1 = add.addition(num1, num2)
        elif operation == "-" or operation == "substraction":
            num1 = sub.substraction(num1, num2)
        elif operation == "*" or operation == "multiplication":
            num1 = mul.multiplication(num1, num2)
        elif operation == "/" or operation == "division":
            num1 = div.division(num1, num2)
        else:
            print("Please enter valid choice")

Calc()