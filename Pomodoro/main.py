import tkinter as tk
from tabnanny import check
from tkinter import Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
finishedSessions = 0
reps = 1
after_id = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global after_id,reps
    window.after_cancel(after_id)
    after_id = None
    canvas.itemconfig(clock, text="00:00")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global after_id, reps, finishedSessions
    if after_id:
        window.after_cancel(after_id)
        after_id = None

    if reps == 1:
        timer.config(text="Work")
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:
        finishedSessions += 1
        timer.config(text="Long Break")
        checkmark.config(text=f"{'✓'*finishedSessions}")
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        finishedSessions += 1
        timer.config(text="Short Break")
        checkmark.config(text=f"{'✓'*finishedSessions}")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text="Work")
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global after_id, reps
    if count>=0:
        after_id = window.after(1000, count_down, count - 1)
        minutes = int(count/60)
        seconds = count % 60
        canvas.itemconfig(clock, text=f"{minutes:02}:{seconds:02}")
    else:
        reps += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
clock = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 26, "bold"))
timer.grid(column=1, row=0)
startButton = Button(text="Start", command=start_timer).grid(column=0, row=2)
resetButton = Button(text="Reset", command=reset_timer).grid(column=2, row=2)
checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
