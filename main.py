BACKGROUND_COLOR = "#B1DDC6"
print("10")
from  tkinter import *
import pandas as pd
import  random
current_card={}

### Function

###
try:
    df=pd.read_csv("words_to_learn.csv")
    df_dict=df.to_dict(orient="records")
except FileNotFoundError:
    df=pd.read_csv("data/french_words.csv")
    df_dict=df.to_dict(orient="records")


def pick_words():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(df_dict)
    canvas.itemconfig(card_back_1, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # df_dict.remove(current_card)
    flip_timer=window.after(3000, show_english)
    # df_1=pd.DataFrame(df_dict)
    # df_1.to_csv("words_to_learn.csv", index=False)
    # canvas.itemconfig(card_title_1, text="English")
    # canvas.itemconfig(card_word_1, text=current_card["English"])

def known_words():
    df_dict.remove(current_card)
    df_1=pd.DataFrame(df_dict)
    df_1.to_csv("words_to_learn.csv", index=False)

    pick_words()


    # print(df_dict)

    # rand_number=random.choice(range(0,102))
    # French_word=df_dict[rand_number]["French"]
    # Engish_word=df_dict[rand_number]["English"]
    # global French_word
    # global Engish_word
    #
    # print(French_word)
    # print(Engish_word)
    #
    # return French_word, Engish_word



window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# canvas=Canvas(626, 900, bg=BACKGROUND_COLOR)
canvas = Canvas( width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)


card_front=PhotoImage(file="C:/Users/Acer/Desktop/Data Science/udemy/flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="C:/Users/Acer/Desktop/Data Science/udemy/flash-card-project-start/images/card_back.png")
card_back_1=canvas.create_image(400, 263, image=card_front)

# canvas.create_image(400, 263, image=card_back)
card_title=canvas.create_text(400, 150, text="", font=("Ariel", 48, "italic"))
card_word=canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(column=1, row=0, columnspan=2, padx=50, pady=50)


##ENGLISH LANGUAGE CODE


def show_english():
    # current_card=random.choice(df_dict)
    # global card_back

    # card_title = canvas.create_text(400, 150, text="", font=("Ariel", 48, "italic"))
    # card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_back_1, image=card_back)
    # canvas.grid(column=1, row=0, columnspan=2)

# Flip to English after 3 seconds
flip_timer=window.after(3000, show_english)





###BUTTON

cross_img = PhotoImage(file="images/wrong.png")

# Then pass the PhotoImage object to the Button
cross_button = Button(image=cross_img, highlightthickness=0, borderwidth=0, command=pick_words)
cross_button.grid(row=1, column=1, pady=10)


right_img = PhotoImage(file="images/right.png")

# Then pass the PhotoImage object to the Button
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=known_words)
right_button.grid(row=1, column=2, pady=10)

pick_words()

    #




# print(df.head())

# for index, row in df.iterrows():















window.mainloop()