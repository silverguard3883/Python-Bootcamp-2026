from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_over = False

while not game_over:
    screen.update()
    time.sleep(0.5)
    snake.move()

    """Detecting collisions"""
    if snake.snake_head.distance(food) < 15:
        food.move()
        snake.extend_snake()
        scoreboard.increase_score()

    """Snake hits a wall"""
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280:
        scoreboard.reset_score()

    """Snake hits its tail"""
    for segment in snake.snake_segments[1:]:                #Slices segments, bypassing first segment
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()



screen.exitonclick()




