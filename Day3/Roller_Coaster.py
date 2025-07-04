print("Hello, Welcome to our fun roller coaster ride. Hope you will enjoy our ride")
height = int(input("Please tell what your height in cm:\n"))
if height > 120:
    print("You are eliglble for ride")
    age = int(input("Please tell us your age: "))
    bill = 0
    if age < 12:
        print("Children will be charged 5 dollars")
        bill = 5

    elif age >= 12 and age <18:
        print("Teenagers will be charged 7 dollars")
        bill = 7

    elif age >= 45 and age <=55:
        bill = 0
        print("Ride is free for you")
    
    else:
        print("Adults will be charged 12 dollars")
        bill = 12

    wants_photo = str(input("Would like to photograph your experience? (Y/N): "))

    if wants_photo == "y":
        bill += 3

    print(f"You bill is {bill}")

else:
    print("Sorry, but you are not eligible to take ride")