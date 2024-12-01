import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
player.spawnTurtle()

carManager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move, "space")

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count == 6:
        count = 0
        carManager.createCar()
    carManager.moveCar()
    if not carManager.checkCollision(player):
        game_is_on = False
    count += 1
screen.exitonclick()
# Things to finish
#
