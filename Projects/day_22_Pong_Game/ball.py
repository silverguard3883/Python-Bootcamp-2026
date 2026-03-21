from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed = 0.1

    def move(self):
        next_x = self.xcor() + self.x_movement
        next_y = self.ycor() + self.y_movement
        self.goto(next_x, next_y)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()





