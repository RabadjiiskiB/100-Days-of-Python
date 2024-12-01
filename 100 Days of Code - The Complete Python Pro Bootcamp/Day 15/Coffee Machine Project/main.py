MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO 2  Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3 Print report.
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.

money = 0.0

chosenDrink = ""
print("Welcome to Coffee Machine!")
userI = input("What would you like? Espresso, Latte, Cappuccino? ")
while userI != "Off":
    if userI == "Report":
        print(f"Water: {resources.get('water')} \nMilk: {resources.get('milk')} \nCoffee: {resources.get('coffee')}")
    elif userI == "Stock":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100

    else:
        print("Needed ingredients: ")
        for key, value in MENU[f"{userI}"]["ingredients"].items():
            if value > resources.get(key):
                print(f"Not enough {key}: {resources.get(key)}")
                break
            print(f"{key}: {value}")

        print(f"{MENU[userI]['cost']}")

        money += float(input("how much quarters do you have? "))*0.25
        money += float(input("how much dimes do you have? "))*0.10
        money += float(input("how much nicks do you have? "))*0.05
        money += float(input("how much pennies do you have? "))*0.01
        print(round(money, 2))

        if money >= MENU[userI]['cost']:
            print(f"Making a {userI}")
            money -= MENU[userI]['cost']
            for key, value in MENU[f"{userI}"]["ingredients"].items():
                resources[key] -= value
            if money != 0:
                print(f"{money}$ change left")
                money = 0
                print(f"Water: {resources.get('water')} \nMilk: {resources.get('milk')} \nCoffee: {resources.get('coffee')}")
    userI = input("Would you like something else? Espresso, Latte, Cappuccino? ")
print("Thank you!")