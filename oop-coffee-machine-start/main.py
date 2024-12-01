from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1 TODO Print report
# 2 TODO Check resources sufficient?
# 3 TODO Process coins
# 4 TODO Check transaction successful?
# 5 TODO Make coffee

coffeMaker = CoffeeMaker()
menu = Menu()
coffeMaker.report()
moneyMachine = MoneyMachine()

choice = input(f"What would you like {menu.get_items()}: ")
drink = menu.find_drink(choice)
print(f"The drink costs {drink.cost}$")
if coffeMaker.is_resource_sufficient(drink):
    if moneyMachine.make_payment(drink.cost):
        coffeMaker.make_coffee(drink)
        print("Thank you!")
        coffeMaker.report()
        moneyMachine.report()
    else:
        print(f"Sorry, you don't have enough money!")
else:
    print("Sorry there is not enough milk")


