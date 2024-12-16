import tkinter as tk
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genPass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    passEntry.insert(0,password)
    passEntry.clipboard_clear()
    passEntry.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePass():

    if not websiteEntry.get() or not userEntry.get() or not passEntry.get():
        messagebox.showerror(title="Empty field", message="Don't leave empty fields pls")
    else:
        website = websiteEntry.get()
        email = userEntry.get()
        password = passEntry.get()
        toSave = messagebox.askokcancel(title=website, message=f"These are the details: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if toSave:
            with open("passwords.txt", "a") as f:
                f.write(f"{website} / {email} / {password} \n")
                websiteEntry.delete(0,'end')
                userEntry.delete(0,'end')
                passEntry.delete(0,'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=20,pady=20)
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1)

# Labels
websiteLabel = tk.Label(text="Website:").grid(row=1,column=0)
userLabel = tk.Label(text="Email/Username").grid(row=2)
passLabel = tk.Label(text="Password:").grid(row=3)

# Entries
websiteEntry = tk.Entry(width=35)
websiteEntry.grid(column=1,row=1,columnspan=2, sticky="EW")
websiteEntry.focus()
userEntry = tk.Entry(width=35)
userEntry.grid(column=1,row=2,columnspan=2, sticky="EW")
passEntry = tk.Entry(width=21)
passEntry.grid(column=1,row=3, sticky="EW")
# Buttons
genPassButton = tk.Button(text="Generate Password", command=genPass)
genPassButton.grid(column=2,row=3, sticky="EW")
addPassButton = tk.Button(text="Add", width=36, command=savePass)
addPassButton.grid(column=1,row=4,columnspan=2, sticky="EW")
window.mainloop()