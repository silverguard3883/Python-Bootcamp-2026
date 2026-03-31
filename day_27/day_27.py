import tkinter
from tkinter import Entry

window = tkinter.Tk()           #Opens a window, similar to screen form turtle

window.title("My First GUI")
window.minsize(500, 500)


#Label
label = tkinter.Label(text="I'm a label", font=("Arial", 25, "bold"))


label.pack()                    #Places label on screen. Can modify orientation, placement, etc.

label["text"] = "New Text"
label.config(text="New Text")

#Button

def button_clicked():
    print("I got clicked")
    label.config(text="Button got clicked")
    new_text = input.get()
    label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_clicked())
button.pack()


#Entry

input = Entry(width=20)
input.pack()
print(input.get())


#Place
"""Used for precise positioning"""
label.place(x=100, y=100)
button.place(x=200, y=-300)
input.place(x=-200, y=300)

#Grid
"""Divides window into a grid"""
label.grid(column=1, row=1)
button.grid(column=2, row=2)
input.grid(column=3, row=6)


"""
Functions with unlimited positional arguments

def function(*args):
    for n in args:
        print(n)

"""
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6,7,8,9))


"""
Functions with unlimited keyword arguments
"""
def calculate(n, **kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
    print(kwargs["add"])

calculate(add=3, multiply=5)


class Car:                                                  #Using kwargs in classes
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Chevrolet", model="Cavalier")

window.mainloop()               #Should always go at end of code



