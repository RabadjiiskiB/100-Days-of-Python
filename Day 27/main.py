import tkinter as tk


def calc():
    print(int(input.get()))
    km = int(input.get()) * 1.609344
    kmLabel.config(text=f"{km:.2f}")

window = tk.Tk()
window.title("Converter")
window.minsize(500, 300)

input = tk.Entry()
input.grid(column=2, row=1)
input.insert(0, "0")
miles = tk.Label(text="Miles")
miles.grid(column=3, row=1)
kilometers = tk.Label(text="Km")
kilometers.grid(column=3, row=2)
calculate = tk.Button(text="Calculate", command=calc)
calculate.grid(column=2, row=3)
label1 = tk.Label(text="is equal to")
label1.grid(column=1, row=2)
kmLabel = tk.Label(text="0")
kmLabel.grid(column=2, row=2)

window.mainloop()
