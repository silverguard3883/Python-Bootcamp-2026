from tkinter import *
from flashcard import FlashcardApp

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcard App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, pady=(0, 20))

app = FlashcardApp(window, canvas)

wrong_button = Button(window,image=app.wrong_image,highlightthickness=0,bd=0, command=app.mark_wrong)
wrong_button.grid(row=1, column=0, padx=20)

right_button = Button(window,image=app.right_image,highlightthickness=0,bd=0,command=app.mark_right)
right_button.grid(row=1, column=1, padx=20)

app.next_card()

window.mainloop()