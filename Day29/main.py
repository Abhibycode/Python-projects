import tkinter
from tkinter import PhotoImage
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    characters = ['@', '#', '$', '%', '&', '*']
    numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = [choice(alphabets) for _ in range(6, 10)]
    chars = [choice(characters) for _ in range(2, 4)]
    nums = [choice(numbers_list) for _ in range(2, 4)]
    password_list = letter + chars + nums
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_name_input.get()
    user = e_username_input.get()
    passwords = password_input.get()

    if len(website) == 0 or len(user) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="empty data", message="You haven't entered all details")
    else:
        is_okay = messagebox.askokcancel(title="details", message=f"Website: {website}\nUser: {user}\nPassword: {passwords}\n\nPlease confirm to save")
        if is_okay:
            with open (file="user_info.txt", mode="a") as user_info:
                user_info.write(f"{website} |{user} | {passwords}" + "\n")
                web_name_input.delete(0, tkinter.END)
                e_username_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #


#Window Setup
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Image
canvas = tkinter.Canvas(height=200, width=200)
image_holder = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= image_holder)
canvas.grid(row=0, column=1)

#website name
web_label = tkinter.Label(window, text="Website")
web_label.grid(row=1, column=0, sticky="E")

web_name_input = tkinter.Entry(window, width=50)
web_name_input.grid(row=1, column=1, columnspan=2, sticky="W")
web_name_input.focus()


#Email/username
e_username_label = tkinter.Label(window, text="Email/Username")
e_username_label.grid(row=2, column=0, sticky="E")

e_username_input = tkinter.Entry(window, width=50)
e_username_input.grid(row=2, column=1, columnspan=2, sticky="W")


#Password
password_label = tkinter.Label(window, text="Password")
password_label.grid(row=3, column=0, sticky="E")

password_input = tkinter.Entry(window, width=25)
password_input.grid(row=3, column=1, sticky="W")

password_generator = tkinter.Button(text="Generate Password", command=generate_password)
password_generator.grid(row=3, column=2, sticky="E")

#add button
add_info = tkinter.Button(window, width=36, text="Add", command=save)
add_info.grid(row=4,column=1, columnspan=2)








window.mainloop()