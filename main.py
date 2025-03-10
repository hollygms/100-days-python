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

#variables
machine_money = 0.00
machine_on = True

#functions
def report():
    for key, value in resources.items():
        print(f"{key.title()}: {value}")
    print(f"Money: ${machine_money:.2f}")

def check_resources(drink):
    """Takes drink order, returns true or false"""
    for key in MENU[drink]["ingredients"]:
        if resources[key] < MENU[drink]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def process_money():
    """asks input on money, returns it"""
    quarters = float(input("Quarters: ")) * 0.25
    dimes = float(input("Dimes: ")) * 0.1
    nickles = float(input("Nickles: ")) * 0.05
    pennies = float(input("Pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


def make_change(user_money, cost):
    """checks if user money is greater than or equal to cost of drink"""
    if user_money >= cost:
        return True
    else:
        return False

def make_drink(drink):
    """takes drink order, subtracts the ingredients from machine resources, returns the cost of drink"""
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    return MENU[drink]["cost"]


#main function
def machine_working(drink):
    """takes a drink order, checks if we have resources and user money, outputs the money we got from sale"""
    cost = MENU[drink]["cost"]
    if check_resources(drink):
        print(f"Total cost is {cost:.2f}")
        user_money = process_money()
        if make_change(user_money, cost):
            change = user_money - cost
            print(f"Your change: ${change:.2f}")
            print(f"Here's your {drink}. Enjoy! ☕️")
            return cost
        else:
            print("Sorry that's not enough money. Money refunded.")
            return 0
    else:
        return 0


#main machine loop
while machine_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "off":
        machine_on = False
    elif prompt == "report":
        report()
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        machine_money += machine_working(prompt)
    else:
        print("Please enter a valid drink.")


