from turtle import Turtle

MOVE_SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x, y=0)
            x -= 20
            self.snake_segments.append(new_segment)

    def add_segment(self, position):
        self.snake_segments.append(Turtle(shape="square"))

    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for segment_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_number - 1].xcor()
            new_y = self.snake_segments[segment_number - 1].ycor()
            self.snake_segments[segment_number].goto(new_x, new_y)
        self.snake_head.forward(MOVE_SPEED)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)









