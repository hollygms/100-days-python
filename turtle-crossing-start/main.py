import time
import turtle
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = Scoreboard()



screen.listen() #check for keybindings
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move(scoreboard.level)

    if player.crossed_finish_line():
        scoreboard.update_score()



    #collide with car
    for car in car_manager.cars:
        if player.distance(car) < 20 and player.ycor() - car.ycor() < 10:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()
