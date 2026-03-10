from colorgram import *
import turtle as t_module
import random

extracted_colors = colorgram.extract("image.jfif", 30)
rgb_colors = []
t_module.colormode(255)

for color in extracted_colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    
    extracted_color_value = (red, green, blue)
    
    rgb_colors.append(extracted_color_value)

#print(rgb_colors)

pointer = t_module.Turtle()
pointer.hideturtle()
pointer.speed("fastest")
pointer.penup()
pointer.setheading(225)
pointer.forward(250)
pointer.setheading(0)

number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    pointer.dot(20, random.choice(rgb_colors))
    pointer.forward(50)
    
    if dot_count % 10 == 0:
        pointer.setheading(90)
        pointer.forward(50)
        pointer.setheading(180)
        pointer.forward(500)

screen = t_module.Screen()
screen.exitonclick()







