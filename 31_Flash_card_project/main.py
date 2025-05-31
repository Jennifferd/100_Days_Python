""""This program will generate flash cards in French and after 3 secs will show the back
    of the card (the English meaning), if you know the word you click the check mark and
    then the word will be deleted from the list of words to learn, if you don't know click
    the x and the word will be kept"""
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    words_csv = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_csv = pandas.read_csv("./data/french_words.csv")

to_learn = words_csv.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def delete_word():
    to_learn.remove(current_card)
    df_to_learn = pandas.DataFrame(to_learn)
    df_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=delete_word)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
