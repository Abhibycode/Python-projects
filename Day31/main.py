import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

#Pandas
try:
    data = pandas.read_csv(fr"C:\Users\Abhishek\Desktop\100 days of python\Day31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(fr"C:\Users\Abhishek\Desktop\100 days of python\Day31\data\German.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# ---------------------------------------------- Backed Part ------------------------------------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text ="German")
    canvas.itemconfig(card_word, text = current_card["German"])
    flip_timer = window.after(3000, func=solution_card)



def solution_card():
    canvas.itemconfig(card_title, text= "English", fill="Green")
    canvas.itemconfig(card_word, text = current_card["in English"], fill="Green")
    canvas.itemconfig(card_background, image=front_card_img)

# ---------------------------------------------- Save Progress -----------------------------------#
def known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("/data/words_to_learn.csv")

    next_card()

# ---------------------------------------------- UI Setup ----------------------------------------#
#Window set
window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=solution_card)

#Flash card
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_card_image = PhotoImage(file=fr"C:\Users\Abhishek\Desktop\100 days of python\Day31\images\card_back.png")
front_card_img = PhotoImage(file=fr"C:\Users\Abhishek\Desktop\100 days of python\Day31\images\card_front.png")
card_background = canvas.create_image(400, 263, image=back_card_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

#Wrong button
wrong_img = PhotoImage(file=fr"C:\Users\Abhishek\Desktop\100 days of python\Day31\images\wrong.png")
unknown_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness = 0, command=next_card)
unknown_button.grid(row=1, column=0, sticky="E")

#Correct button
correct_img = PhotoImage(file=fr"C:\Users\Abhishek\Desktop\100 days of python\Day31\images\right.png")
known_button = Button(image=correct_img, bg=BACKGROUND_COLOR, highlightthickness = 0, command=known)
known_button.grid(row=1, column=1, sticky="E")

next_card()

window.mainloop()