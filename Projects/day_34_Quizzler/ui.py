from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=30, bg=THEME_COLOR)

        self.score_label = Label(text="Score:", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=300, bg="white")
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            150,
            text="",
            font=("Arial", 20, "italic"),
            width=250
        )

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(command=self.true_answer)
        self.true_button["image"] = true_image
        self.true_button["text"] = "True"
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(command=self.false_answer)
        self.false_button["image"] = false_image
        self.false_button["text"] = "False"
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="That's the end of the quiz!")
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"

    def true_answer(self):
        self.give_feedback((self.quiz.check_answer("true")))

    def false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
