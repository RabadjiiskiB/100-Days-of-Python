import random
import colorgram
from turtle import Turtle, Screen, colormode

colors = colorgram.extract('image.jpg', 20)

colorList = []
for color in colors:
    colorTuple = color.rgb
    colorList.append((colorTuple[0], colorTuple[1], colorTuple[2]))

timmy = Turtle()
timmy.shape("turtle")
colormode(255)
timmy.speed("fastest")
timmy.up()
timmy.hideturtle()
timmy.goto(-400, -300)


def draw_dot(timmy, color):
    timmy.dot(20,color)
    timmy.forward(50)


def dottedLine():
    for i in range(10):
        draw_dot(timmy, random.choice(colorList))


def moveTurtle():
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)


def draw_shape(turtle, sides):
    for i in range(sides):
        turtle.forward(100)
        turtle.left(360 / sides)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


for i in range(5):
    dottedLine()
    moveTurtle()

# while True:
#     timmy.forward(20)
#     timmy.left(random.randint(1,5)*90)
#     timmy.color(random_color())

# for i in range(3,10):
#     draw_shape(timmy, i)

screen = Screen()
print(screen.screensize())
screen.exitonclick()
