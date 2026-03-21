from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    """Detect collisions with wall"""
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    """Detect collisions with paddle"""
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """Check if left player scores"""
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()



screen.exitonclick()


