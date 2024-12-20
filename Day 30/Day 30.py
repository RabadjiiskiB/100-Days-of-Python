
# FileNotFound
try:
    with open("Day 31.txt") as file:
        file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File found.")
