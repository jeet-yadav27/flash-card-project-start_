from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=900, height=626, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="C:/Users/Acer/Desktop/Data Science/udemy/flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="C:/Users/Acer/Desktop/Data Science/udemy/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, borderwidth=0)
cross_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0)
right_button.grid(row=1, column=1)

window.mainloop()