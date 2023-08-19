import tkinter

window = tkinter.Tk()
window.title("HEHEHE eltit is backwards")  # title of the window
window.minsize(width=600, height=600)  # minimal size of the window
# label
my_label = tkinter.Label(text="GURRWAAA", font=('Times New Roman', 20, 'normal'))
#specyfying how the label is displayed
my_label.pack(side='left')  # allows the label to be shown



window.mainloop()
