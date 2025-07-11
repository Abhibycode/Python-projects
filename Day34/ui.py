import tkinter
from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz =  quiz_brain
        self.window = tkinter.Tk()
        self.window.title("True or False")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(self.window, text=f"Score: 0", fg="white", bg=THEME_COLOR , font=("Ariel", 10, "bold"))
        self.score_label.grid(row=0, column=1, sticky="E")

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some Question",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 10, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file=fr"C:\Users\Abhishek\Desktop\100 days of python\Day34\images\true.png")
        wrong_img = PhotoImage(file=fr"C:\Users\Abhishek\Desktop\100 days of python\Day34\images\false.png")

        self.true = tkinter.Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.true.grid(row=2, column=0)

        self.wrong = tkinter.Button(image=wrong_img, highlightthickness=0, command=self.false_press)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You reached end of quiz")
            self.true.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)