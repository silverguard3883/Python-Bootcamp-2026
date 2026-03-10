from tkinter import *
from turtle import *
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape = shape("arrow")
timmy_the_turtle.color = ("blue")


for _ in range(4):                          #Draws a box
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    
for _ in range(15):                         #Draws a dashed line
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "maroon", "black", "gold", "silver"]
sides = 4

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb_tuple = (red, green, blue)
    return rgb_tuple
        
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap_size)
    
        
        
        
for shape_side_n in range(3, 11):
    timmy_the_turtle.color(random.choice(colors).lower())
    draw_shape(shape_side_n)

directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

for _ in range(200):                                            #Created random colored straight path
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
    

timmy_the_turtle.speed("fastest")

    

#Python tuples
#Similar to lists
# Example (1, 3, 8)
# my_tuple = (1, 3, 8)
#print(my_tuple[0])

#Tuples are IMMUTABLE; they cannot be changed
#You can convert a tuple to a list if changes MUST be made; the immutability prevents accidental modifications














screen = Screen()
screen.exitonclick()