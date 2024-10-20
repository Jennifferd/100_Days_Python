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

def print_report():
    """ Prints a report of the resources """
    for key in resources:
        print(f"{key}: {resources[key]}")

def resources_sufficient(desired_coffe: str) -> bool:
    """ Checks if there is enough resources for the desired coffee """
    for ingredient in MENU[desired_coffe]["ingredients"]:
        if resources[ingredient] < MENU[desired_coffe]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins(desired_coffe: str) -> float:
    """ Convertes the coins to money """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_paid = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_paid

def transaction(money_inserted: float, desired_coffe: str) -> int:
    """" Checks if the money inserted and make transaction """
    money_needed = MENU[desired_coffe]["cost"]
    change = round(money_inserted - money_needed, 2)
    if change == 0:
        print(f"Here is your {desired_coffe} ☕️. Enjoy!")
        resources["money"] += money_needed
        deduct_ingredients(desired_coffe)
    elif change > 0:
        print(f"Here is ${change} in change.")
        print(f"Here is your {desired_coffe} ☕️. Enjoy!")
        resources["money"] += money_needed
        deduct_ingredients(desired_coffe)
    else:
        print("Sorry that's not enough money. Money refunded.")

def deduct_ingredients(desired_coffe: str):
    """" deduce the ingredients from the resources"""
    for ingridient in MENU[desired_coffe]["ingredients"]:
        resources[ingridient] -= MENU[desired_coffe]["ingredients"][ingridient]

def coffee_machine():
    coffee_on = True
    resources["money"] = 0
    MENU["espresso"]["ingredients"]["milk"] = 0
    while coffee_on:
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if option == "report":
            print_report()
        elif option == "latte" or option == "espresso" or option == "cappuccino":
            coffee = option
            if resources_sufficient(coffee):
                paid = process_coins(coffee)
                transaction(paid,coffee)
        elif option == "off":
            coffee_on = False

coffee_machine()
