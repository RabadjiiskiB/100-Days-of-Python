from turtle import Screen, done
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
exitGame = False

def resetGame():
    scoreboard.goto(0, 270)
    scoreboard.reset()
    snake.reset_snake()
    global game_is_on
    game_is_on = True


def exit_Game():
    global exitGame, game_is_on
    exitGame = True
    game_is_on = False
    scoreboard.game_over()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(resetGame, "r")
screen.onkey(exit_Game, "s")

while not exitGame:
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            game_is_on = False

        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

    while not game_is_on and not exitGame:
        screen.update()
        time.sleep(0.1)

print("Hello")
screen.exitonclick()

