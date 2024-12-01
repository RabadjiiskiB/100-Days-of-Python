import random
from turtle import Turtle, Screen
import turtleController as ctrl
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
# screen.listen()
# screen.onkey(key='w', fun=lambda: ctrl.move_forward(tim))
# screen.onkey(key='s', fun=lambda: ctrl.move_backward(tim))
# screen.onkey(key='a', fun=lambda: ctrl.turn_left(tim))
# screen.onkey(key='d', fun=lambda: ctrl.turn_right(tim))
# screen.onkey(key='c', fun=lambda: ctrl.clear(tim))

screen.setup(500, 400)
userI = screen.textinput("Make your bet", "Which turtle will win the race?")
isRaceOn = True

for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].up()
    turtles[i].color(colors[i])
    turtles[i].goto(-230, -100+i*30)

while isRaceOn:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            print(f"The {turtle.pencolor()} turtle won")
            if turtle.pencolor() == userI:
                print("You win")
            else:
                print("You lost")
            isRaceOn = False

# screen.exitonclick()