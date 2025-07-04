import tkinter
from tkinter import Entry

FONT = ("Ariel", 12, "bold")

window = tkinter.Tk()
window.title("This is window")
window.minsize(width=700, height=700)

#Label
my_label = tkinter.Label(text="This is my label", font=FONT)
my_label.pack()
my_label["text"] = "This is an update"


#Button
button = tkinter.Button()
button["text"] = "click me"

#Entry
input_box = Entry(width=100)
input_box.pack()

def button_clicked():
    content = input_box.get()
    my_label.place(x = 100, y =100)
    my_label["text"] = content

button["command"] = button_clicked
button.pack()




window.mainloop()