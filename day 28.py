import tkinter
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
#window settings
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)
check_mark = "✔"
# label
title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60))
title.grid(column=1, row=0)
# background
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # allows to get the image as the background of the GUI
back_image = tkinter.PhotoImage(file='tomato.png')  # allows to get the image from the file
# tomato image at the back
canvas.create_image(100, 112, image=back_image)  # image is put on specified position
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)
#buttons
start_button = tkinter.Button(text='START', highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="RESET", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text=check_mark, fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
