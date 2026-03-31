from tkinter import *

def convert():
    miles = float(mile_input.get())
    km = miles * 1.609
    km_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Mile to Km Converter")

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)


window.mainloop()