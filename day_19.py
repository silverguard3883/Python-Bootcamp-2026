import random
from turtle import Turtle, Screen

# tim_the_turtle = Turtle()
screen = Screen()

def move_forward():
    tim_the_turtle.forward(5)

def move_backward():
    tim_the_turtle.backward(5)

def turn_left():
    tim_the_turtle.left(5)

def turn_right():
    tim_the_turtle.right(5)

def clear_screen():
    tim_the_turtle.clear()
    tim_the_turtle.penup()
    tim_the_turtle.home()
    tim_the_turtle.pendown()


# # screen.listen()
# screen.onkey(key="Right", fun=move_forward)
# screen.exitonclick()

#
# """Etch-A-Sketch"""
#
# screen.listen()
# screen.onkey(move_forward,  "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left,  "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_screen, "c")
# screen.exitonclick()

"""Turtle Race"""
screen.setup(500, 400)
turtle_wager = screen.textinput(title="Place your bet!", prompt="Which turtle will win? Enter a color: ")
colors = ["red", "orange", "indigo", "green", "blue", "purple"]
race_over = False
turtles_in_race = []

x = -230
y = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x, y)
    y = y + 50
    turtles_in_race.append(new_turtle)

while race_over is False:

    for turtle in turtles_in_race:

        if turtle.xcor() > 230:
            race_over = True
            winner = turtle.pencolor()
            print(f"{winner} has won!")
            if turtle_wager == winner:
               print("You win!")
            else:
               print("You lose!")

        turtle_speed = random.randint(0, 20)
        turtle.forward(turtle_speed)















screen.exitonclick()