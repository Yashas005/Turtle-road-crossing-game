import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up,"w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    for c in car.all_cars:
        if c.distance(player)<20:
            scoreboard.game_over()
            game_is_on = False
    if player.is_at_finish_line():
        player.goto_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()