import time

from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen, Turtle
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
snake = Snake()
screen.listen()
food = Food()
score = Scoreboard()

screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.turn(270), "s")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        game_is_on = False
        score.game_over()
        break

    if snake.head.distance(food) < 15:
        print("You ate the food")
        food.refresh()
        score.addToScore()
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            score.game_over()


screen.exitonclick()
