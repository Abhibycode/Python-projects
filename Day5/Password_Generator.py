import random
symbols = [ "*", "#", "/", "@", "!"]
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

password = []

passcode = ""

#Method1:

Length_of_password = int(input("Please enter length of password: \n"))
number_of_nums = int(input("How many numbers you want to add: \n"))
number_of_symbols = int(input("How many symbols you want to add: \n"))

for i in range(Length_of_password-number_of_nums-number_of_symbols):
    counter = random.randint(0, len(alphabets)-1)
    password.append(alphabets[counter])

for i in range(number_of_nums):
    counter = random.randint(0, 9)
    password.append(counter)

for i in range(number_of_symbols):
    counter = random.randint(0, len(symbols)-1)
    password.append(symbols[counter])

print(password)
random.shuffle(password)
print("".join(map(str, password)))


#Method2:

for i in range(Length_of_password-number_of_symbols-number_of_nums):
    passcode += random.choice(alphabets)
for i in range(number_of_nums):
    passcode += str(random.choice(numbers))
for i in range(number_of_symbols):
    passcode += random.choice(symbols)

random.choice(passcode)
print(passcode)