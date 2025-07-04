    import tkinter
import math
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text = "")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN  * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS%2 == 0)):
            mark = "✓"

        check_mark.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #


#Window setup
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=100, bg=YELLOW)



#Adding image
canvas = tkinter.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


#timer_label
timer_label = tkinter.Label(window, text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)


#Start button
start_button = tkinter.Button(window, text="Start", bg="White", command=start_timer)
start_button.grid(row=2, column=0)

#Reset button
reset_button = tkinter.Button(window, text="Reset", bg="White", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = tkinter.Label(window, font= (FONT_NAME, 15), fg = GREEN, bg=YELLOW)
check_mark.grid(row=2, column=1)

window.mainloop()