import tkinter

window = tkinter.Tk()
window.title("Miles to KM")
window.minsize(width=100, height=100)

#Inputbox
input_value = tkinter.Entry(window, width=10)
input_value.insert(0, "0")
input_value.grid(row=0, column=1)

#Miles Label beside input box
Miles_label = tkinter.Label(text="Miles")
Miles_label.grid(row=0, column=2)

#is equal to
is_equal_to = tkinter.Label(window, text = "Is equal to ")
is_equal_to.grid(row=1, column=0)

#Result value label
result_label = tkinter.Label(window, text = "0")
result_label.grid(row=1, column=1)

#KM label
km_label = tkinter.Label(window, text="KM")
km_label.grid(row=1, column=2)

#Calculate button


def cal():
    miles = float(input_value.get())
    result = miles * 1.60934
    result_label["text"] = result
calculate = tkinter.Button(window, text="Calculate", command=cal)
calculate.grid(row=2, column=1)


window.mainloop()