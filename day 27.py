import tkinter

window = tkinter.Tk()
window.title("retarded units to kilometers converter")  # title of the window
window.minsize(width=400, height=300)  # minimal size of the window
# window.config(padx=20, pady=20)  # padding
"""
# label
my_label = tkinter.Label(text="GURRWAAA", font=('Times New Roman', 20, 'normal'))
#specyfying how the label is displayed
# my_label.pack()  # packs the widgets starting from the top to bottom
# my_label['text'] = 'new text'  # changing the text of the label
# my_label.place(x=0, y=0)  # places the label on the specified coordinates
my_label.grid(column=0, row=0)  # places the widget according the specified position on the grid
grid, place, pack is not compatible with each other. Only one can be used
# buttons
def click():
    my_label['text'] = New_input.get()  # gets the input and makes it the label name


button = tkinter.Button(text='KLIKNIJ MNIE!', command=click)
button.grid(column=1, row=1)
#button nr 2
button2 = tkinter.Button(text='METALE CIĘŻKIE ZABIJAJĄ!', command=click)
button2.grid(column=2, row=0)
# Input
New_input = tkinter.Entry(width=20)
New_input.grid(column=3, row=2)
"""
my_label1 = tkinter.Label(text="         ", font=('Times New Roman', 12, 'normal'))
my_label1.grid(column=0, row=0)
my_label = tkinter.Label(text="Miles to km converter", font=('Times New Roman', 14, 'normal'))
my_label.grid(column=1, row=0)

def click():
    kilometers['text'] = f"{round(float(miles.get())*1.609344, 2)}"  # gets the input and makes it the label name


button = tkinter.Button(text='Convert', command=click)
button.grid(column=1, row=1)
miles_label = tkinter.Label(text=f"Miles: ", font=('Times New Roman', 12, 'normal'))
miles_label.grid(column=0, row=2)
miles = tkinter.Entry(width=10)
miles.grid(column=1, row=2)
kilometers_label = tkinter.Label(text=f"Kilometers: ", font=('Times New Roman', 12, 'normal'))
kilometers_label.grid(column=0, row=3)
kilometers = tkinter.Label(text=f" ", font=('Times New Roman', 12, 'normal'))
kilometers.grid(column=1, row=3)


window.mainloop()

