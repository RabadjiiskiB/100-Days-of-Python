from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.score = 0
        self.pencolor('white')
        self.ht()
        self.print()

    def print(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align='center', font=('Arial', 24, 'bold'))
    def addToScore(self):
        self.score += 1
        self.print()
