from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

script_dir = os.path.dirname(os.path.abspath(__file__))


csv_path = os.path.join(script_dir, "data", "french_words.csv")
words_to_learn_path = os.path.join(script_dir, "data", "words_to_learn.csv")
card_front_path = os.path.join(script_dir, "image", "card_front.png")
card_back_path = os.path.join(script_dir, "image", "card_back.png")
wrong_image_path = os.path.join(script_dir, "image", "wrong.png")
right_image_path = os.path.join(script_dir, "image", "right.png")

try:
    data = pd.read_csv(words_to_learn_path)
except FileNotFoundError:
    original_data = pd.read_csv(csv_path)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(words_to_learn_path, index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=card_front_path)
card_back_img = PhotoImage(file=card_back_path)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=wrong_image_path)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

check_image = PhotoImage(file=right_image_path)
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=0)

next_card()

window.mainloop()
