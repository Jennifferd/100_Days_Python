from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()

coffee_on = True
while coffee_on:
    option = input(f"What would you like? {menu.get_items()}: ")
    if option == "report":
        coffee_machine.report()
        money_machine.report()
    elif option == "latte" or option == "espresso" or option == "cappuccino":
        coffee = menu.find_drink(option)
        if coffee_machine.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_machine.make_coffee(coffee)
    elif option == "off":
        coffee_on = False
