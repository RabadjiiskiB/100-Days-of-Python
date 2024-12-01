import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard



screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
# This paired with update and sleep allows to stop the animation on everything until it is set up
screen.tracer(0)

player = Paddle(-350)
enemy = Paddle(350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "s")
screen.onkeypress(enemy.up, "Up")
screen.onkeypress(enemy.down, "Down")

game_is_on = True
while game_is_on:

    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(enemy) < 50 and ball.xcor() > 340 or ball.distance(player) < 50 and ball.xcor() < -340:
        ball.deflect()
    elif ball.xcor() > 390:
        print("Enemy loses")
        scoreboard.l_score += 1
        ball.reset_ball()
        scoreboard.update()
    elif ball.xcor() < -390:
        print("Player loses")
        scoreboard.r_score += 1
        ball.reset_ball()
        scoreboard.update()

screen.exitonclick()

