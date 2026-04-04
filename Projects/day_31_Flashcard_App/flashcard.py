from tkinter import Canvas
import pandas
import random


class FlashcardApp:
    def __init__(self, window, canvas: Canvas):
        self.window = window
        self.canvas = canvas
        self.flip_timer = None
        self.current_card = {}

        # Load data
        try:
            data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            data = pandas.read_csv("data/french_words.csv")

        self.to_learn = data.to_dict(orient="records")

        # Load images
        self.card_front_image = self._load_image("images/card_front.png")
        self.card_back_image = self._load_image("images/card_back.png")
        self.right_image = self._load_image("images/correct.png")
        self.wrong_image = self._load_image("images/wrong.png")

        # Build card canvas items once
        self.card_background = self.canvas.create_image(
            400, 263, image=self.card_front_image
        )
        self.card_title = self.canvas.create_text(
            400, 150, text="", font=("Arial", 40, "italic")
        )
        self.card_word = self.canvas.create_text(
            400, 263, text="", font=("Arial", 60, "bold")
        )

    def _load_image(self, path):
        from tkinter import PhotoImage
        return PhotoImage(file=path)

    def show_front(self, word):
        self.canvas.itemconfig(self.card_background, image=self.card_front_image)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=word, fill="black")

    def show_back(self, word):
        self.canvas.itemconfig(self.card_background, image=self.card_back_image)
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=word, fill="white")

    def next_card(self):
        if self.flip_timer is not None:
            self.window.after_cancel(self.flip_timer)

        if not self.to_learn:
            self.canvas.itemconfig(self.card_background, image=self.card_front_image)
            self.canvas.itemconfig(self.card_title, text="Done", fill="black")
            self.canvas.itemconfig(self.card_word, text="No more words", fill="black")
            return

        self.current_card = random.choice(self.to_learn)
        self.show_front(self.current_card["French"])
        self.flip_timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        if self.current_card:
            self.show_back(self.current_card["English"])

    def mark_right(self):
        if not self.current_card:
            return

        if self.current_card in self.to_learn:
            self.to_learn.remove(self.current_card)

        self.save_progress()
        self.next_card()

    def mark_wrong(self):
        if not self.current_card:
            return

        self.save_progress()
        self.next_card()

    def save_progress(self):
        data = pandas.DataFrame(self.to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)