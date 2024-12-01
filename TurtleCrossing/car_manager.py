import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.garage = []
        self.ht()

    def createCar(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.teleport(270, random.randint(-250, 250))
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        self.garage.append(new_car)

    def moveCar(self):
        for car in self.garage:
            car.forward(10)

    def checkCollision(self, player):
        for car in self.garage:
            if car.distance(player) < 20:
                print("Aahh hit")
                return False
            else:
                return True

