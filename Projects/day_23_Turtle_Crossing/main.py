import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Turtle Jumper")

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_traffic()
    car.move()


    """Detect turtle getting run over"""
    for traffic in car.traffic:
        if traffic.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    """Detect turtle getting to other side"""
    if player.finish_line():
        scoreboard.increase_score()
        player.reset_player()
        car.increase_difficulty()


screen.exitonclick()