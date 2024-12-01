
products = [ "01.Potato", "02.Fish", "03.Apple"  "04.Orange", "05.Milk", "06.Music"]
for product in products:
    print(product)

print("")
programRuns = True
while programRuns is True:
    choice = input("1 for making an order / 2 for List of orders / 3 for Help / 4 for Request to cancel order: ")
    if choice == "1":
        code = input("Enter 2 digit product code or 00 to finish the order: ")
        order = ""
        while code != "00":
            code = input("Enter 2 digit product code or 00 to finish the order: ")
            order += code

        if order != "":
            print(order)
    else:
        programRuns = False
        pass