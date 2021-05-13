import tkinter as tk

temp_c = None
temp_f = None

def convert():

    global temp_c
    global temp_f

    try:
        val = temp_c.get()
        temp_f.set((val * 9.0 / 5) + 32)
    except:
        pass

def clear_text():
   entry_celsius.delete(0, tk.END)


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("700x500")

frame = tk.Frame(root)

frame.pack(fill=tk.BOTH, expand=True)
frame.configure(background="blue")

frame.columnconfigure(5, weight=5)
frame.rowconfigure(2, weight=2)

temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()


entry_celsius = tk.Entry(frame, width=15, font="times 20", bg="light blue", textvariable=temp_c)
label_unitc = tk.Label(frame, width=0, font="times 20", bg="light blue", text="°C")
label_equal = tk.Label(frame, width=0, font="times 20", bg="light blue", text="is equal to:")
label_fahrenheit = tk.Label(frame, width=15, font="times 20", bg="light blue", textvariable=temp_f)
label_unitf = tk.Label(frame, width=0, font="times 20", bg="light blue", text="°F")
button_convert = tk.Button(frame, width=30, bd=10, font="times 20", bg="light blue", text="Convert", command=convert)
button_clear = tk.Button(frame, width=5, font="times 20", bg="light blue", text="Clear", command=clear_text)

entry_celsius.place(x=210, y=5)
label_unitc.place(x=415, y=5)
label_equal.place(x=270, y=50)
label_fahrenheit.place(x=210, y=100)
label_unitf.place(x=415, y=100)
button_convert.place(x=140, y=170)
button_clear.place(x=580, y=175)

entry_celsius.focus()

root.mainloop()
