import turtle

import pandas as pd

states = pd.read_csv("50_states.csv")
stateNames = states["state"].tolist()
xcoor = states["x"].tolist()
ycoor = states["y"].tolist()
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
print(stateNames)
guessed = []
writer = turtle.Turtle()
writer.penup()
writer.ht()
while len(guessed) < 50:
    answer = screen.textinput(f"{len(guessed)}/50", "Hello").title()
    if answer == "Exit":
        states_to_learn = [state for state in stateNames if state not in guessed]
        df = pd.DataFrame(states_to_learn)
        df.to_csv("States_to_learn.csv")
        break
    elif answer in stateNames:
        x = xcoor[stateNames.index(answer)]
        y = ycoor[stateNames.index(answer)]
        writer.goto(x, y)
        writer.write(answer)
        guessed.append(answer)
    elif answer in stateNames and not "Exit":
        print("not ok")




screen.exitonclick()
