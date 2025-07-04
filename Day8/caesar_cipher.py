alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(message, shifts):
    generated_message = ""
    for letter in message:
        num = alphabets.index(letter)
        new_position =  (num+shifts) % 26
        generated_message += alphabets[new_position]
    print(generated_message)

def decrypt(message, shifts):
    generated_message = ""
    for letter in message:
        num = alphabets.index(letter)
        new_position =  (num-shifts) % 26
        generated_message += alphabets[new_position]
    print(generated_message)

question = str(input("You wise to continue:\n")).lower()

while question =="yes":
    requirement = input("Please enter 'encrypt' to encrypt message and 'decrypt' to decrypt message:\n")
    if requirement == "encrypt":
        encrypt(message=input("Enter message:\n"), shifts=int(input("Enter shifts:\n")))
    elif requirement == "decrypt":
        decrypt(message=input("Enter message:\n"), shifts=int(input("Enter shifts:\n")))
    elif requirement =="no":
        break
    else:
        print("You please enter valid choice (encrypt/decrypt)")
    