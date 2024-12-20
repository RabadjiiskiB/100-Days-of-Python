
# FileNotFound
# try:
#     with open("Day 30.txt") as file:
#         file.read()
#         dict = {"key": "value"}
#         print(dict["dwas"])
# except FileNotFoundError:
#     print("File not found.")
# except KeyError as error:
#     print(f"The key {error} does not exist.")
# else:
#     print("File found.")
# finally:
#     print("Finished.")

height = float(input("Enter your height in metres: "))
weight = int(input("Enter your weight in kilograms: "))

if height > 3:
    raise ValueError("Human height is too high")

bmi = weight / height ** 2
