from tkinter import *
from tkinter import Entry, Button, Label, END


root = tk.Tk()


root.geometry("250x150")
root.title("Jordan Does Maths")


Label_1 = Label(root, text="Number 1: ")
Label_1 = Entry(root, width=30)

Label_2 = Entry(root, width=30)
Label_2 = Label(root, text="Number 2: ")

Label_1.place(x=10, y=0)
Label_1.place(x=50, y=0)
Label_2.place(x=10, y=50)
Label_2.place(x=50, y=50)


results_Label = Label(root, text="results: ")
results_entry = Entry(root, state=("random"))

results_Label.place(x=18, y=80)
results_entry.place(x=50, y=80)


def add_two_numbers():
    the_sum = float(entry1.get()) + float(entry2.get())
    results_entry.config(state)

top.mainloop()