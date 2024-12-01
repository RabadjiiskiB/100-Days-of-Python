from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 8)
        self.color("white")
        self.penup()
        self.left(90)
        self.goto(x, 0)
        self.moveUp = False
        self.moveUp = False
        self.up()
        self.down()

    def moveUp(self):
        if not self.moveUp:
            True
        else:
            False

    def moveDown(self):
        if not self.moveDown:
            True
        else:
            False

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
